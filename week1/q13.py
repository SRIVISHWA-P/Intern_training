#single number

arr=[]
#populating the array
n=int(input("How many elements will you enter :"))
for i in range(n):
    e=eval(input("Enter the element %d :"%(i+1)))
    arr.append(e)
print("The elements of the array :")

for i in arr:
    if(arr.count(i)==1):
        print("The single number in the array is %d"%i)
