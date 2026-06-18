print("\t\tcheck whether a string is pallendrome or not")
str=input("enter the string you need to check:")
l = len(str)
i = 0
j = l-1
count=0
print(l)
while( i < j):
    if(str[i]!=str[j]):
        count=count+1
        i=i+1
        j=j-1
    else:
        i=i+1
        j=j-1
if(count==0):
    print("the string is pallendrome.")
else:
    print("the string is not pallendrome.")


