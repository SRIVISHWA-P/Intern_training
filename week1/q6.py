# Find if a number is an armstrong number 

n=int(input("Enter a number :"))
l=len(str(n))
sum=0
temp=n


for i in range(l):
    sum+=pow((temp%10),l)
    temp//=10

if n==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")