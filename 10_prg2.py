def game():
    return 49

score =game()
with open("hiscore.txt")as f:
    hiscore =f.read()
if(hiscore ==''):
    with open("hiscore.txt","w")as f:
        f.write(str(score))
if(int (int(hiscore)<score) ):
    with open("hiscore.txt","w")as f:
        f.write(str(score))