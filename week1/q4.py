#Series GP

a=int(input("Enter the first term of the series 'a' :"))
r=int(input("Enter the common ratio of the series 'r' :"))
n=int(input("Enter the n value(not zero):"))
print("\nThe series is :")
count=1
while(count!=n+1):
    print(a*(pow(r,count-1)),end=' ')
    count+=1