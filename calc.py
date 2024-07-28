import argparse

parser = argparse.ArgumentParser(description="A basic calculator")
parser.add_argument(
    "-a", "--add", help="add numbers", type=float, nargs="+", action="append"
)
parser.add_argument(
    "-s", "--subtract", help="subtract numbers", type=float, nargs="+", action="append"
)
parser.add_argument(
    "-m", "--multiply", help="multiply numbers", type=float, nargs="+", action="append"
)
parser.add_argument(
    "-d", "--divide", help="divide numbers", type=float, nargs="+", action="append"
)

args = parser.parse_args()
result = 0
for list in args.add:
    for num in list:
        result = result + float(num)

for list in args.subtract:
    for num in list:
        result = result - float(num)

for list in args.multiply:
    for num in list:
        result = result * float(num)

for list in args.divide:
    for num in list:
        if int(num) == 0:
            continue
        result = result / float(num)
print(result)
