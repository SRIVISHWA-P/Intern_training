# Reverse of a number

n=int(input("Enter a number :"))
l=len(str(n))
sum=0
for i in range(l):
    sum=sum*10+(n%10)
    n//=10
print("\nThe reverse of the number %d is %d"%(n,sum))
