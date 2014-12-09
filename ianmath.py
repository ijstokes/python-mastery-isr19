" A module of Ian's special math functions "

_version = 0.4
_author  = 'Ian Stokes-Rees'

def sin(x):
    " small angle approximation for x "
    return x

def rand():
    " return a 'random' number "
    return 66

def adder(a, b):
    " add together some values "
    result = a + b
    return result

def main():
    print "sin:", sin(0.6)
    print "rand:", rand()
    print "fav:", fav

fav = 25

if __name__ == '__main__':
    # we're executing this instead of
    # importing it
    main()
