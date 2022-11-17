'''Given an array of penalties fine[], an array of car numbers car[], and also the date.
The task is to find the total fine which will be collected on the given date. 
Fine is collected from odd-numbered cars on even dates and vice versa.'''


n=int(input("Enter the no of cars="))
car=[int(input("Enter a car number :")) for i in range(n)]
print("\n")
fine=[int(input("Enter a fine :")) for i in range(n)]
date=int(input("enter the date:"))

if date%2==0:
    sum=0
    for i in range(n):
        if car[i]%2!=0:
            sum+=fine[i]
    print("Total fine = ",sum)
else:
    sum=0
    for i in range(n):
        if car[i]%2==0:
            sum+=fine[i]
    print("Total fine = ",sum)
    