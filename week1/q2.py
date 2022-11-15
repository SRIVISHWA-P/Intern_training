#2) Get the month and year and print the number of days in that month

m=input("Enter the name of month :")
y=int(input("Enter the year :"))
temp=m.lower()

#leap year function
def leap(y):
    if((y%4==0 or y%400==0) and y%100!=0):
        return True



if temp=='february':
    if leap(y)==True:
        print("\nThe number of days in february is 29 in the year %d"%y)
    else:
        print("\nThe number of days in february is 28 in the year %d"%y)
else:
    if(temp=='january' or temp=='march' or temp=='may'or temp=='july' or m=='august' or temp=='october' or temp=='december'):
        print("\nThe month %s has 31 days in the year %d"%(m,y))
    else:
        print("\nThe month %s has 30 days in the year %d"%(m,y))