# Check if the given elements are in the given range
A=int(input("Enter the starting number of the range :"))
B=int(input("Enter the ending number of the range :"))
arr=[]
#populating the array
n=int(input("How many elements will you enter :"))
for i in range(n):
    e=eval(input("Enter the element %d :"%(i+1)))
    arr.append(e)
print("The elements of the array :")

for i in range(A,B+1):
    if i not in arr:
        print("No")
        break
else:
    print("Yes")