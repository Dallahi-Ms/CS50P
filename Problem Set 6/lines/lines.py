import sys

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
if len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

lines = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif not line.strip():
                pass
            else:
                lines += 1
    print(lines)

except FileNotFoundError:
    sys.exit("File does not exist")
