#Series GP

a=int(input("Enter the first term of the series 'a' :"))
r=int(input("Enter the common ratio of the series 'r' :"))
n=int(input("Enter the n value(not zero):"))
term=a*(pow(r,n-1))
print("\nThe %dth term of the series is %d"%(n,term))