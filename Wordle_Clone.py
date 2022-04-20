# Attempting to make a wordle clone

# have list of 5 letter words
# randomly choose one word from list to be key word
# ask for 5 letter input, compare to each word in list
# if the word exists in the list
#       compare guess word to key word
#       if letter exists in word, print lowercase
#       if letter is correct (with location) print uppercase
#       for complete incorrect guesses print "_" into location

# ex: if keyword is POWER
#   guess is PLOTS
#   should return P_o__

# else say word is invalid, ask for new guess (if word not in list)


import random

guessLibrary = open("valid-wordle-words.txt", "r").read().splitlines()
answerLibrary = open("wordle-answers-alphabetical.txt", "r").read().splitlines()


keyword = random.choice(answerLibrary)
keyArray = list(keyword)

numGuess = 1


### Welcome message ###
print("Welcome to Ericle")

while(numGuess < 7):  # while user has remaining guesses

    answerArray = ["_", "_", "_", "_", "_"]
    
    guess = input("Guess a 5 letter word (Lowercase): ")
    guessArray = list(guess)

    for i in guessLibrary:  # checking if word is in list
        if guess == i:
            valid = True
            numGuess += 1  # increment guess ONLY IF word in list
            break  # finds that word is in list, breaks for loop to begin checking letters
        else:
            valid = False  # finds that word is not at index, continues comparing

    if valid == True: # if word in list, check letters
        if guess == keyword:
            print("Correct! The word is: " + keyword.upper())
            break
        
        for j in range(len(keyArray)):
            if keyArray[j] == guessArray[j]: #  if letter and location correct
                answerArray[j] = keyArray[j].upper() #  fill answer array with correct letter (CAPITAL)
            else:
                answerArray[j] = "_"
                
        for k in range(len(keyArray)):
            if guessArray[k] in keyArray:  # need to make this so that it only enters letter once if it appears once in the keyword !!
                keyOccur = keyArray.count(guessArray[k])  # count number of times letter appears in keyword
                answerOccur = answerArray.count(guessArray[k]) + answerArray.count(guessArray[k].upper())
                if keyOccur > answerOccur and answerArray[k] == '_':
                    answerArray[k] = guessArray[k].lower()
            else:
                answerArray[k] = "_"

        ansString = ""
        answer = ansString.join(answerArray)
        print(answer)
      
    else:
        print("Invalid guess, try again.")
        

if numGuess > 7:
    print("You lose, the word was: " + keyword)
#print("Out of guesses, you lose.")  # need to move this so that it doesnt print every time           

# for loop
    # run through keyword, compare to guess
    # if correct letter, correct spot, capital letter
    # else _

# for loop
    # if guess character in keyword
    # count occurences in keyword, count occurences in answer

    # if occur in keyword > occur in answer, and answer = _, enter lowercase




    
