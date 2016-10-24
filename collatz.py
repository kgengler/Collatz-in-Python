import sys
import argparse

#create cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("num", type=int)
parser.add_argument("-s", "--steps", help="print out steps in conjecture", action="store_true")
args = parser.parse_args()

count = 0
num = args.num

print("\nCollatz Conjecture for %d" % num)

#conjecture logic
while num != 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1
    count += 1
    if args.steps:
        print("Step %d: %d" % (count, num))
print("Reached 1 in %d steps.\n" % count)
