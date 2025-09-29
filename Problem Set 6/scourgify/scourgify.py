import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith('csv'):
    sys.exit("Not a CSV file")

file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1) as file:
        reader = csv.DictReader(file)
        with open(file2, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row['name'].split(', ')
                house = row['house']
                writer.writerow({"first": first, "last": last, "house": house})


except FileNotFoundError:
    sys.exit(f"Could not read {file1}")
