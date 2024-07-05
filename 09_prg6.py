def word_and_split(string):
    new=string.replace("Harry"," ")
    return new.strip()

str1=input("Enter String")
print(word_and_split(str1))