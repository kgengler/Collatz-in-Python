#!/usr/bin/env python
import argparse

def hotpo(n):
    """Divide by 2 if even, otherwise triple and add 1
    
    Keyword arguments:
    n -- the number to check
    """
    return n / 2 if n % 2 == 0 else 3 * n + 1

def collatz(n, acc = 0, print_steps = False):
    """This function will return the number of HOTPO steps required to reach 1 
    
    Keyword arguments:
    n -- the number to run the collatz conjecture against
    acc -- the current step in the operation (default 0)
    print_steps -- print the current step in the console
    """
    if print_steps:
        print("Step %d: %d" % (acc, n))
        
    return acc if n == 1 else collatz(hotpo(n), acc + 1, print_steps)

if __name__ == '__main__':
    # create cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    parser.add_argument("-s", "--steps", help="print out steps in conjecture", action="store_true")
    args = parser.parse_args()

    num = args.num
    count = collatz(num, print_steps = args.steps)

    print("\nCollatz Conjecture for %d" % num)
    print("Reached 1 in %d steps.\n" % count)
