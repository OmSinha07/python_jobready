'''Guess the number game'''

import random
randno = random.randint(1,100)
userGuess =None
guesses=0
while(userGuess!=randno):
    userGuess =int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randno):
        print("You guesses it right!")
    else:
        if(userGuess>randno):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a greater number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt") as f:
    hiscore = int(f.read())
    if(guesses<hiscore):
        print("You have just broken your own highscore")
        with open("hiscore.txt","w")as f:
            f.write(str(guesses))