#!/usr/bin/env python
from random    import randint
from functools import partial

# some constants
POOL = int(1e5) # size of pool we are selecting numbers from
TCNT = int(1e4) # number of tickets we'll issue
WCNT = int(1e3) # number of winning numbers will generate


def main(pool, tcnt, wcnt):
    lotto = partial(randint, 1, pool)
    # lotto = lambda : randint(1, pool)

    tickets = [lotto() for draw in range(tcnt)] # create TCNT tickets
    uniqtix = set(tickets)                      # get unique set of tickets
    wintix  = {lotto() for draw in range(wcnt)} # get unique winners from WCNT draws
    # len(wintix) <= wcnt

    winnums = wintix & uniqtix                  # unique winning numbers

    winpeople = [ticket for ticket in tickets if ticket in winnums]

    print("Winning numbers:", len(winnums))
    print("Winning people:", len(winpeople))

def getargs():

    import argparse # from the standard library

    parser = argparse.ArgumentParser(description='Play the lottery')

    parser.add_argument('pool', metavar='POOL', type=int,
                       help='size of pool to select numbers from')
    parser.add_argument('tcnt', metavar='TCNT', type=int,
                       help='number of tickets issued')
    parser.add_argument('wcnt', metavar='WCNT', type=int,
                       help='number of winning numbers selected')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    import sys
    args = getargs() # tuple unpacking
    main(args.pool, args.tcnt, args.wcnt)