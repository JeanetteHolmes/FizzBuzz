

def fizz_buzz ():
    """ () -> 

    Happily pretend that a computer can play FizzBuzz until 100.
    Note that mistakes are not inserted intentionally, as it is not
    in the nature of a computer to take a shot.  In fact mistakes
    resulting in the computer being required to intake alcohol
    might result in the computer passing out both immediately and
    permanently, and is beyond the scope of this exercise.
    
"""
        
    for i in range (1, 101):
        if ((i%3 == 0) and (i%5 == 0)):
            print ('fizzbuzz')
        elif (i%3 == 0):
            print ('fizz')
        elif (i%5 == 0):
            print ('buzz')
        else:
            print (i)

if (__name__ == "__main__"):
    import doctest
    doctest.testmod()

