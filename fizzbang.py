

def fizz_bang (n):
    """ (n) -> 

    Happily pretend that a computer can play FizzBang until n.
    Note that mistakes are not inserted intentionally, as it is not
    in the nature of a computer to get drunk.  In fact mistakes
    resulting in the computer being required to intake alcohol
    might result in the computer passing out both immediately and
    permanently, and is beyond the scope of this exercise.
    
    >>> fizz_bang (2)
    1
    2
    >>> fizz_bang (3)
    1
    2
    fizz
    >>> fizz_bang (7)
    1
    2
    fizz
    4
    bang
    fizz
    7
    >>> fizz_bang (17)
    1
    2
    fizz
    4
    bang
    fizz
    7
    8
    fizz
    bang
    11
    fizz
    13
    14
    fizzbang
    16
    17
    
"""
        
    for i in range (1, n+1):
        if ((i%3 == 0) and (i%5 == 0)):
            print ('fizzbang')
        elif (i%3 == 0):
            print ('fizz')
        elif (i%5 == 0):
            print ('bang')
        else:
            print (i)

if (__name__ == "__main__"):
    import doctest
    doctest.testmod()

