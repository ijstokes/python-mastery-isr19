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
    if len(sys.argv) != 4:
        print("usage:", sys.argv[0], "POOL TCNT WCNT", """

    POOL size of pool to select numbers from
    TCNT number of tickets issued
    WCNT number of winning numbers selected
""")
        sys.exit(1)
    else:
        pool = int(sys.argv[1])
        tcnt = int(sys.argv[2])
        wcnt = int(sys.argv[3])
        return pool, tcnt, wcnt # tuple packing 3 arguments extracted from CLI

if __name__ == '__main__':
    import sys
    pool, tcnt, wcnt = getargs() # tuple unpacking
    main(pool, tcnt, wcnt)