words=["donkey","kaddu","mote"]

with open("sample1.txt") as f:
    con=f.read()

for word in words:
    con=con.replace(word,"####@")
    print(con)
    with open("sample1.txt","w") as f:
        f.write(con)