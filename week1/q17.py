arr=[]
#populating the array
n=int(input("How many elements will you enter :"))
for i in range(n):
    e=eval(input("Enter the element %d :"%(i+1)))
    arr.append(e)
print("The elements of the array :")

odd_sum=0
even_sum=0

for i in range(n):
    if i%2==0:
        even_sum+=arr[i]
    else:
        odd_sum+=arr[i]
print("The odd position sum is %d\nThe even position sum is %d"%(odd_sum,even_sum))