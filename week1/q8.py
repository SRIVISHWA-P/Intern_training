# Print n fibonacci terms using iteration and recursion

n=int(input("Enter the n value :"))
print("The fibonacci series is :")
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a=0
    b=1
    c=0
    count=1
    while(count!=n):
        c=a+b
        print(c,end=',')
        a=b
        b=c
        count+=1
