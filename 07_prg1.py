a=int(input("Enter numbers"))
b=int(input("Enter numbers"))
c=int(input("Enter numbers"))
d=int(input("Enter numbers"))
if(a>b and a>c and a>d):
 print(a)
elif(b>c and b>d and b>a):
 print(b)
elif(c>a and c>b and c>d):
 print(c)
else:
 print(d)