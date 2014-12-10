#!/usr/bin/env python
from random    import randint
from functools import partial

# some constants
POOL = int(1e5) # size of pool we are selecting numbers from
TCNT = int(1e4) # number of tickets we'll issue
WCNT = int(1e3) # number of winning numbers will generate

lotto = partial(randint, 1, POOL)
# lotto = lambda : randint(1, POOL)

def main(pool, tcnt, wcnt):
    tickets = [lotto() for draw in range(TCNT)] # create TCNT tickets
    uniqtix = set(tickets)                      # get unique set of tickets
    wintix  = {lotto() for draw in range(WCNT)} # get unique winners from WCNT draws
    # len(wintix) <= WCNT

    winnums = wintix & uniqtix                  # unique winning numbers

    winpeople = [ticket for ticket in tickets if ticket in winnums]

    print("Winning numbers:", len(winnums))
    print("Winning people:", len(winpeople))

if __name__ == '__main__':
    main(POOL, TCNT, WCNT)