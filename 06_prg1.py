mydict={
    "pankha":"fan",
    "kursi":"chair",
    "vastu":"item"
}
print("the keys for dictionary  :",mydict.keys())
a=input("enter the word\n")
print("found the english translation for the word ",a)
print("the english translation for the word is",mydict.get(a))
