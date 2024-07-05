import os
old="t.txt"
new="n.txt"
with open(old) as f:
    con=f.read()

with open(new,"w") as f:
    f.write(con)

os.remove(old)
