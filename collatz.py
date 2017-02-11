#!/usr/bin/env python
import argparse

def hotpo(n):
    """Divide by 2 if even, otherwise triple and add 1
    
    Keyword arguments:
    n -- the number to check
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def collatz(n, acc = 0):
    """This function will return the number of HOTPO steps required to reach 1 
    
    Keyword arguments:
    n -- the number to run the collatz conjecture against
    acc -- the current step in the operation (default 0)
    """
    if n == 1:
        return acc
    else:
        return collatz(hotpo(n), acc + 1)

if __name__ == '__main__':
    # create cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    args = parser.parse_args()

    num = args.num
    count = collatz(num)

    print("\nCollatz Conjecture for %d" % num)
    print("Reached 1 in %d steps.\n" % count)

