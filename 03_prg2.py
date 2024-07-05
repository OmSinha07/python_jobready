name=input("enter name ")
date=input("Enter date ")
letter=''' Dear <|name|>,
You are selected!

Date: <|date|>
'''
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)