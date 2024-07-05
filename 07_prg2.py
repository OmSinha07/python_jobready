s1=int(input("Enter marks"))
s2=int(input("Enter marks"))
s3=int(input("Enter marks"))
if(s1<33 or s2<33 or s3<33):
    print("You are failed")
elif(s1+s2+s3)/3 <40:
    print("failed")
else:
    print("passed")
