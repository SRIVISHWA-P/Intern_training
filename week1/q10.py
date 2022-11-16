#Check if two strings are anagrams

a=input("Enter the string1 :")
b=input("Enter the string2 :")
if(sorted(a)==sorted(b)):
    print("The given strings are anagrams")
else:
    print("The given strings are not anagrams")