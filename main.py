import os
import sys
import importlib.util
from aocd import get_data, submit
from aocd.models import Puzzle
from datetime import datetime
from dotenv import load_dotenv
from contextlib import redirect_stdout, redirect_stderr

load_dotenv()

def run_advent_of_code(day: int, part: int, input_file: str):
    day_path = str(day).zfill(2)
    module_name = f"{day_path}/part_{part}.py"
    module_spec = importlib.util.spec_from_file_location(f"day{day}_part{part}", module_name)
    module = importlib.util.module_from_spec(module_spec)
    input_file = os.path.join(day_path, input_file)
    with open(input_file, 'r') as f, \
         redirect_stdout(sys.stdout), redirect_stderr(sys.stderr):
        sys.stdin = f
        module_spec.loader.exec_module(module)

def fetch_aoc_data(day: int, year: int = None):
    """Fetch puzzle input from Advent of Code."""
    year = year or datetime.now().year
    return get_data(day=day, year=year)

def create_advent_of_code(day: int, year: int = None):
    """Create necessary files and fetch data from Advent of Code."""
    day_path = str(day).zfill(2)
    token = os.environ.get("AOC_SESSION")

    if not token:
        raise Exception("TOKEN environment variable not set.")

    os.makedirs(day_path, exist_ok=True)

    input_file = os.path.join(day_path, "input.txt")
    open(os.path.join(day_path, "sample.txt"), 'a').close()

    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        input_data = fetch_aoc_data(day, year)
        with open(input_file, 'w') as f:
            f.write(input_data)

    template = ("import sys\n"
                "data = sys.stdin.readlines()\n\n"
                "sol = 0\n\n"
                "# TODO: Solve the problem!\n"
                "# Your solution goes here\n\n"
                "print(sol)\n")

    for part in ['1', '2']:
        with open(os.path.join(day_path, f"part_{part}.py"), 'w') as file:
            file.write(template)

def submit_solution(day: int, part: str, year: int = None):
    """Automatically submit the last printed integer as the solution."""
    try:
        puzzle = Puzzle(year=year or datetime.now().year, day=day)
        latest_output = puzzle.latest_output(part)
        if latest_output.isdigit():
            submit(latest_output, part=part, day=day, year=puzzle.year)
            print(f"Submitted {latest_output} for day {day} part {part}")
        else:
            print(f"No valid integer output found for day {day} part {part}")
    except Exception as e:
        print(f"Error submitting solution: {e}")

def main():
    year = datetime.now().year
    day = datetime.now().day

    if len(sys.argv) == 1:
        print("Usage: python main.py [run|new|submit] [day] [part] [input_file]")
        sys.exit(1)

    func = sys.argv[1]
    if func == "run":
        if len(sys.argv) != 5:
            print("Usage: python main.py run [day] [part] [input_file]")
            sys.exit(1)
        day = int(sys.argv[2])
        part = int(sys.argv[3])
        input_file = sys.argv[4]
        run_advent_of_code(day=day, part=part, input_file=input_file)
    elif func == "new":
        if len(sys.argv) != 3:
            print("Defaulting to current day")
            create_advent_of_code(day, year)
        else:
            create_advent_of_code(int(sys.argv[2]), year)
    elif func == "submit":
        if len(sys.argv) != 4:
            print("Usage: python main.py submit [day] [part]")
            sys.exit(1)
        submit_solution(int(sys.argv[2]), sys.argv[3], year)
    else:
        print("Invalid function. Use 'run', 'new', or 'submit'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
