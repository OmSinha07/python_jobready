comment=input("enter the text")
spam = False
if (comment == "make alot of money"):
    spam= True
elif(comment == "subscribe now"):
    spam=True
elif(comment == "comment now"):
     spam =True
else:
    spam=False
if(spam==True):
    print("spam comment")
else:
    print("not")