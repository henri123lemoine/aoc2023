import os
import sys
import requests
import importlib.util
from datetime import datetime
from dotenv import load_dotenv
from contextlib import redirect_stdout, redirect_stderr

load_dotenv()


def run_advent_of_code(day, part, input_file):
    module_name = f"{day}/part_{part}.py"
    module_spec = importlib.util.spec_from_file_location(f"day{day}_part{part}", module_name)

    module = importlib.util.module_from_spec(module_spec)
    with open(input_file, 'r') as f, \
         redirect_stdout(sys.stdout), redirect_stderr(sys.stderr):
        sys.stdin = f
        module_spec.loader.exec_module(module)


def fetch_aoc_data(year: int, day: int, token: str):
    """Fetch puzzle input and description from Advent of Code."""
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {'Cookie': f'session={token}'}
    input_response = requests.get(input_url, headers=headers)
    return input_response.text


def create_advent_of_code(day: int):
    """Create necessary files and fetch data from Advent of Code."""
    day_path = str(day).zfill(2)
    year = datetime.now().year
    token = os.environ.get("TOKEN")

    if not token:
        raise Exception("TOKEN environment variable not set.")

    os.makedirs(day_path, exist_ok=True)

    input_file = os.path.join(day_path, "input.txt")
    open(os.path.join(day_path, "sample.txt"), 'a').close()

    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        input_data = fetch_aoc_data(year, day, token)
        with open(input_file, 'w') as f:
            f.write(input_data)

    template = ("import sys\n"
                "data = sys.stdin.readlines()\n\n"
                "sol = 0\n\n"
                "# TODO: Solve the problem!\n"
                "# Your solution goes here\n\n"
                "print(f\"sol: {sol}\")\n")

    for part in ['1', '2']:
        with open(os.path.join(day_path, f"part_{part}.py"), 'w') as file:
            file.write(template)


def main():
    if len(sys.argv) == 1:
        latest_day = sorted([f for f in os.listdir(".") if f.isdigit()], key=int)[-1]
        for part in ['1', '2']:
            run_advent_of_code(latest_day, part, os.path.join(latest_day, "input.txt"))
    elif len(sys.argv) > 1:
        func = sys.argv[1]
        if func == "run":
            if len(sys.argv) != 5:
                print("Usage: python main.py run [day] [part] [input_file]")
                sys.exit(1)
            run_advent_of_code(sys.argv[2], sys.argv[3], os.path.join(sys.argv[2], sys.argv[4]))
        elif func == "new":
            if len(sys.argv) != 3:
                print("Usage: python main.py new [day]")
                sys.exit(1)
            create_advent_of_code(sys.argv[2])
        else:
            print("Usage: python main.py [run|new]")
            sys.exit(1)

if __name__ == "__main__":
    main()
