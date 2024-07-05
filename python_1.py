def head(fpath):
    with open(fpath) as file:
        i=0
        for line in file:
            print(file)
            i+=1
            if i==5:
                break

head(r"C:/Users/KIIT/Desktop/python(AI_ML)/Pandas_Transforms and aggregation/bezdekIris.data")