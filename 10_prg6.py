with open("text.txt") as f:
    con=f.read()
with open("copy.txt","w")as f:
    f.write(con)