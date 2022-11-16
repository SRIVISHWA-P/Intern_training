# Given an array, find the second largest number
arr=[]
#populating the array
n=int(input("How many elements will you enter :"))
for i in range(n):
    e=eval(input("Enter the element %d :"%(i+1)))
    arr.append(e)
print("The elements of the array :")

#finding largest number
large=arr[0]
l_pos=arr.index(large)
for i in arr:
    if i>large:
        large=i
        l_pos=arr.index(i)

#finding second large
sec_large=arr[l_pos-1]
for j in arr:
	if((j>sec_large) and j!=large):
		sec_large=j
if(large==sec_large):
    print("There is no second large element")
else:
    print("The second largest element in an array is %d"%sec_large)