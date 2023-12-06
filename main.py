import sys
import os
import importlib.util
from contextlib import redirect_stdout, redirect_stderr

def run_advent_of_code(day, part, input_file):
    module_name = f"{day}/part_{part}.py"
    module_spec = importlib.util.spec_from_file_location(f"day{day}_part{part}", module_name)

    module = importlib.util.module_from_spec(module_spec)
    with open(input_file, 'r') as f, \
         redirect_stdout(sys.stdout), redirect_stderr(sys.stderr):
        sys.stdin = f
        module_spec.loader.exec_module(module)

def create_advent_of_code(day):
    os.makedirs(day, exist_ok=True)

    open(os.path.join(day, "input.txt"), 'a').close()
    open(os.path.join(day, "sample.txt"), 'a').close()

    template = ("import sys\n"
                "data = sys.stdin.readlines()\n\n"
                "sol = 0\n\n"
                "# TODO: Solve the problem!\n"
                "# Your solution goes here\n\n"
                "print(f\"sol: {sol}\")\n")

    for part in ['1', '2']:
        with open(os.path.join(day, f"part_{part}.py"), 'w') as file:
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
