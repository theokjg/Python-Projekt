###
# Välja ett tal

correctNumber= 6
numOfGuesses = 3

# Be om en siffra

while (numOfGuesses > 0):
    print ("guess a number")
    guess = int (input())
    print("you guessed")
    print(guess)

    numOfGuesses -= 1

    # Kolla om siffran är större, mindre eller lika

    if (guess > correctNumber):
        print("you guessed too large. Try again.")
        #, mindre eller lika
    elif (guess < correctNumber):
        print("you guessed too small. Try again.")
    else:
        print("you guessed corerect")
        numOfGuesses = 0


# göra tre gånger