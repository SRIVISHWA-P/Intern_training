#Given a string, count the number of alphabets in it

s=input("Enter a string :")
count=0
for i in s:
    if((i>'A' and i<'Z') or (i>'a' and i<'z')):
        count+=1
print("The nukber of alphabets in the given string is %d"%count)