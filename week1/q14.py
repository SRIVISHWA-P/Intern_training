'''Given a street of N houses (a row of houses), each house having K amount of money kept inside;
 now there is a thief who is going to steal this moneybut he has a constraint/rule that 
 he cannot steal/rob two adjacent houses. Find the maximum money he can rob.'''
N=int(input("Enter the number of houses :"))
K=int(input("Enter the amount of money kept in each house :"))
if N%2==0:
    print("The maximum money he can rob is %d"%((N//2)*K))            
else:
    print("The maximum money he can rob is %d"%(((N//2)+1)*K))
