print("\t\tsum of first n numbers")
num= int(input("enter the range:"))
i=1
sumeven=0
sumodd=0
while i<=num:
    if(i%2 == 0):
        sumeven=sumeven+i
        i=i+1
    else:
        sumodd=sumodd+i
        i=i+1

print("sum of the even numbers are:",sumeven)
print("sum of the odd numbers are:",sumodd)