def rec_sum(num):
    if(num==0):
        return 0
    else:
        return num + rec_sum(num-1)
    
num=int(input("Enter numbers"))
print(rec_sum(num))