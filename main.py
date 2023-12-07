import os
import sys
import importlib.util
from io import StringIO
from aocd import submit
from aocd.models import Puzzle, User
from datetime import datetime
from dotenv import load_dotenv
from contextlib import redirect_stdout, redirect_stderr

load_dotenv()


def run_advent_of_code(day: int, part: int, year: int, input_file: str):
    day_path = str(day).zfill(2)
    module_name = f"{day_path}/part_{part}.py"
    module_spec = importlib.util.spec_from_file_location(f"day{day}_part{part}", module_name)
    module = importlib.util.module_from_spec(module_spec)
    input_file_path = os.path.join(day_path, input_file)

    # old_stdout = sys.stdout
    # redirected_output = StringIO()
    # sys.stdout = redirected_output

    with open(input_file_path, 'r') as f:#, \
         #redirect_stdout(redirected_output), redirect_stderr(sys.stderr):
        sys.stdin = f
        module_spec.loader.exec_module(module)

    # sys.stdout = old_stdout
    
    # print(f"Day {day} Part {part} Output:")
    # print(redirected_output.getvalue())

    # solution = redirected_output.getvalue().split('\n')[-2]
    # print(f"Day {day} Part {part} Solution attempt: \"{solution}\"")

    # if input_file == 'input.txt':
    #     submit(solution, part="a" if part == 1 else "b", day=day, year=year)


def fetch_aoc_data(day: int, year: int, AOC_SESSION: str = None):
    year = year or datetime.now().year
    user = User(AOC_SESSION)
    return user.get_data(day=day, year=year)


def create_advent_of_code(day: int = None, year: int = None, AOC_SESSION: str = None):
    day = day or datetime.now().day
    day_path = str(day).zfill(2)
    year = year or datetime.now().year

    puzzle = Puzzle(day=day, year=year)
    # if puzzle.is_unlocked:
    #     print(f"Day {day} is already unlocked.")
    #     sys.exit(1)
    
    os.makedirs(day_path, exist_ok=True)
    input_file = os.path.join(day_path, "input.txt")

    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        input_data = fetch_aoc_data(day, year, AOC_SESSION)
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


def main():
    AOC_SESSION = os.environ.get("AOC_SESSION")
    year = datetime.now().year

    if not AOC_SESSION:
        raise Exception("AOC_SESSION environment variable not set.")
    
    if len(sys.argv) == 1:
        print("Usage: python main.py [run|new] [day] [part] [input_file]")
        sys.exit(1)

    func = sys.argv[1]
    if func == "run":
        if len(sys.argv) != 5:
            print("Usage: python main.py run [day] [part] [input_file]")
            sys.exit(1)
        day = int(sys.argv[2])
        part = int(sys.argv[3])
        input_file = sys.argv[4]
        run_advent_of_code(day=day, part=part, input_file=input_file, year=year)
    elif func == "new":
        if len(sys.argv) == 3:
            create_advent_of_code(int(sys.argv[2]), AOC_SESSION=AOC_SESSION)
        else:
            create_advent_of_code(AOC_SESSION=AOC_SESSION)
    else:
        print("Invalid function. Use 'run' or 'new'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
