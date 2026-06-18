print("\t\tReverse the given string")
str=input("enter the string you need to reverse:")
l = len(str)
j = l-1
str1 = []
for i in range(j,-1,-1):
        str1.append(str[i])
        i=i-1

print("the reversed string is:",''.join(str1))