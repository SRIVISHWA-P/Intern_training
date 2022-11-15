#Palindrome String

s=input("Enter a string :")
temp_str=s[::-1]
if s==temp_str:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")