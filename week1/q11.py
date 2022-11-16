n=int(input("How many elements will you enter :"))
arr=[]
for i in range(n):
    e=eval(input("Enter the element %d :"%(i+1)))
    arr.append(e)
print("The elements of the array :")
for j in arr:
    print(j,end='')
rev_arr=[]
for k in range(n-1,-1,-1):
    rev_arr.append(arr[k])
print("\nThe elements of the reversed array :")
for h in rev_arr:
    print(h,end=' ')