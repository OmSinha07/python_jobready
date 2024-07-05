'''SNAKE WATER GUN OR ROCK PAPER SCISSORS GAME WITH COMPUTER'''
import random
def gameWin(comp,you):
    if comp == You:
        return None
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp =='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp =='g':
        if you=='w':
            return True
        elif you=='s':
            return False
    
    
print("Computer's Turn: Snake(s) Water(w) or Gun(g)?")
randNo =random.randint(1,3)
if(randNo==1):
    Comp='s'
if(randNo==2):
    Comp='w'
if(randNo==3):
    Comp='g'
You=input("player 1 Turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(Comp,You)
print(f"Computer's choice {Comp} ")
print(f"Your's choice {You} ")
if a == None:
    print("The game is a tie")
elif a == True:
    print("You Won!")
else:
    print("You lose!")