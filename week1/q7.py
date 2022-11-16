#Search an element in an array
print("\nTo populate the list please enter the elements")
arr=[]
while True:
    n=int(input("Enter an element or enter -1 to stop entering:"))
    if n==-1:
        break
    else:
        arr.append(n)
print("\nThe elements of the list are :\n")
for j in arr:
    print("%d "%j)
x=int(input("\nEnter the element to be searched"))
for k in arr:
    if k==x:
        print("The element %d found in %d"%(k,arr.index(k)))
else:
        print("Element not found")
