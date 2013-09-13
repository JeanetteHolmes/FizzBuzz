import random

def movie_fizz_buzz (n):
    """ (int) -> 

    Happily pretend that a computer can play FizzBuzz until n.

    In this version of the game, the computer chooses a movie and
    selects quotes from that movie instead of using fizz and buzz.
    Why?  Because it can!
    
"""
    
    movie_quotes = [
        ("Princess Bride",
         ["I myself am often surprised at life's little quirks",
          "Hello.  My name is Inigo Montoya.....",
          "Inconceivable!"]),
        ("Star Wars",
         ["Use the Force.",
          "Do or do not.  There is no try.",
          "I am your father."]),
        ("Back to the Future",
         ["I'm your density.",
          "It requires something with a little more kick. Plutonium.",
          "Where we're going, we don't need roads."]),
        ("Lord of the Rings",
         ["Not all those who wander are lost.",
          "We've had one, yes. What about second breakfast?",
          "My precious!!!!!"]),
        ("Star Trek",
         ["Live long and prosper.",
          "Beam us up, Scotty.",
          "Engage."]),
        ("Indiana Jones",
         ["I don't know. I'm making this up as I go.",
          "Snakes. Why did it have to be snakes?",
          "Indiana Jones. I always knew some day you’d come walking back through my door."]),
        ("The Matrix",
         ["Fate, it seems, is not without a sense of irony.",
          "Why, oh, why, didn't I take the blue pill?",
          "There is no spoon."])
        ]

##  randomly choose a movie from the ones defined
    which_movie = random.randint(0,len(movie_quotes)-1)
    
    print ("\nGreat news!  Your movie quotes are from " +
        movie_quotes[which_movie][0] + "\n")

    start_of_range = min (1, n)
    end_of_range = max (1, n+1)
        
    for i in range (start_of_range, end_of_range):
        if ((i%3 == 0) and (i%5 == 0)):
            print (movie_quotes[which_movie][1][2])
        elif (i%3 == 0):
            print (movie_quotes[which_movie][1][1])
        elif (i%5 == 0):
            print (movie_quotes[which_movie][1][0])
        else:
            print (i)


def get_user_input_number (prompt_string: str): 
    """ (string) -> int
    Get a number from user input, using promt_string to prompt the user
    The number must be positive.

"""
    user_number = None
    while not user_number:
        try:
            user_number = int(input (prompt_string))
            assert (user_number > 0)
        except:
            print ("Must be a valid positive number, please try again.")
            user_number = None
    return user_number

def get_players (n, L): 
    """ (int, List of string) -> int
    Get a number of players from the user, return the max name length

    """
    max_len = 0
    for i in range (n):
        if (i != 0):
            print ("You are now ", i, "/", n,
               " of the way to having named all of your players.  \nKeep up the good work!\n")
        player_name = input ("Please enter a player name: ")
        L.append (player_name)
        if (max_len) < len(player_name): max_len = len (player_name)
    return max_len
    
def annoying_fizz_buzz ():
    """ () -> 

    Happily pretend that a computer can play FizzBuzz.

    I imagined what this little game might turn into in a blue-sky meeting
    where flexibility is highly valued, ideas are mostly accepted instead of
    trade-offs being evaluated, and the development people are unable or unwilling
    to push back.  It's not a good dynamic and you might see some resentment from
    the developers leaking out through the user interface.  It ended up seeming
    intentionally annoying.

    This was hilarious to think about, fun to code, and a big pain to test.  There
    is probably more to be done here.
    
    """

#   first the slow painful process of getting all the user input
    print ("\nHello, welcome to fizz_buzz, a fun game for everyone!\n")
    user_name = input ("What is your name?  ")

    print ("\nHello " + user_name + ", get ready for a fun time!\n")
    print ("\nFirst we have a few questions, " + user_name + " .\n")

#   be sure to have the prompts almost but not quite the same to encourage confusion
    fizz_string = input ("What would you like to use for the fizz string? ")
    fizz_number = get_user_input_number("\nWhat would you like to use for the fizz number? ")

    print ("\nGreat job " + user_name + "!  Just a few more questions!\n")

    buzz_string = input ("What would you like to use for the buzz string? ")
    buzz_number = get_user_input_number ("\nWhat would you like to use for the buzz number? ")

    print ("\nGreat job " + user_name + "!  Just a few more questions.\n")
    print ("How about if all of your friends play too?  Doesn't that sound fun?\n")
    
    number_players = get_user_input_number ("\nHow many players would you like to pretend there are? ")

    print ("\nGreat job " + user_name + "!  Time to name the players!\n\n")

#   note that the user is not automatically added.  If you want to be a player you must
#   enter yourself again.  annoying.
    player_list = []
    player_name_max_len = get_players (number_players, player_list)

    start_of_range = get_user_input_number ("\nWhat number would you like to use for the beginning of your game? ")
    end_of_range = get_user_input_number ("\nWhat number would you like to use for the end of your game? ")
#   fix things up so the same loop can work for counting up or counting down
    if (start_of_range < end_of_range):
        incrementation_value = 1
    else:
        incrementation_value = -1

#   some of the questions are apparently only here to annoy the user
    font_to_use = input ("\nWhat font would you like to use?  ")
    print ("Note: Feature not implemented in this version.\n")
    font_size = get_user_input_number ("What font size would be the most fun for your game? ")
    print ("Note: Feature not implemented in this version.\n")

    print ("\nGreat news!  Your game starts now! \n")

#   at last the loop!
    i = start_of_range
    while (i != end_of_range + incrementation_value):
        player = player_list[i%number_players]
        if ((i%fizz_number == 0) and (i%buzz_number == 0)):
            print (player.ljust(player_name_max_len), ' : ', fizz_string, buzz_string)
        elif (i%fizz_number == 0):
            print (player.ljust(player_name_max_len), ' : ', fizz_string)
        elif (i%buzz_number == 0):
            print (player.ljust(player_name_max_len), ' : ', buzz_string)
        else:
            print (player.ljust(player_name_max_len), ' : ', i)
        i = i + incrementation_value


def get_index_to_use (stage_of_game: float, number_strings: int): 
    """ (float, int) -> int

    Figure out the index to use.  In each set of strings, the first one is
    correct, the others are mistakes.  The longer the game has been going,
    the more likely mistakes are.  But this is not a smooth linear function,
    mistakes can happen at any time. So we take the stage of the game and
    multiply by a random number, and convert that into the index to use.
    
"""

    random_factor = random.random()
    probability = stage_of_game * random_factor
    index = int (probability * number_strings)

    return index


def party_fizz_buzz (n):
    """ (int) -> 

    Happily pretend that a computer can play FizzBuzz until n.

    In this version I imagined my old pets playing fizz buzz while the
    humans were gone.  They have somehow liberated their intoxicant of
    choice.  Obviously they can speak while the humans are away.  However
    they get sillier and sillier as the game progresses.  They can still
    count, but they are having trouble saying fizz and buzz.

    This is surprisingly entertaining to run.  This one works with
    negative numbers, but the mistakes are all weighted towards the beginning
    of the game.  So if pets are playing fizzbuzz and they use a negative n,
    they are sobering up.

    
"""

    fizz_strings = ["Fizz", "fzz", "ffiiiiiiz", "fez", "fizzle", "fo shizzle", "fffffff", "fizi", "fizzy yay",
                    "get fizzy with it"]
    fizz_number = 3

    buzz_strings = ["Buzz", "buzzy", "da buzziness", "buzzle", "bbbuz", "BuZzZz"]
    buzz_number = 5
    
    number_players = 4
    player_list = ['Tasha', 'The Fat One', 'The Feisty One', 'The Little One']
    player_name_max_len = 25
        
    start_of_range = min (1, n)
    end_of_range = max (1, n+1)
        
    for i in range (start_of_range, end_of_range):
        player = player_list[i%number_players]
        stage_of_game = i/n

        fizz_index = get_index_to_use (stage_of_game, len (fizz_strings))
        buzz_index = get_index_to_use (stage_of_game, len (buzz_strings))
        
        if ((i%fizz_number == 0) and (i%buzz_number == 0)):
            print (player.ljust(player_name_max_len), ' : ',
                   fizz_strings[fizz_index], buzz_strings[buzz_index])
        elif (i%fizz_number == 0):
            print (player.ljust(player_name_max_len), ' : ',
                   fizz_strings[fizz_index])
        elif (i%buzz_number == 0):
            print (player.ljust(player_name_max_len), ' : ',
                   buzz_strings[buzz_index])
        else:
            print (player.ljust(player_name_max_len), ' : ', i)


if (__name__ == "__main__"):
    import doctest
    doctest.testmod()

