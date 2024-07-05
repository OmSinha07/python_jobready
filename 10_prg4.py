with open("donkey.txt",) as f:
    s=f.read()
    
    s=s.replace("donkey","#####")
    print(s)


with open("donkey.txt","w") as f:
    f.write(s)