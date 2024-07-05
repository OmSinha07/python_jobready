n=3
for i in range (n):
    print("*"*i,end="")
    
print()
for j in range(1,(n+1)):
      if(j%2==0):
        print(" ",end="")
      else:
        print("*",end="")
        
print()
for k in range(n):
   print("*"*k,end="") 