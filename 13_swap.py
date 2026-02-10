arr=[1,2,3,4,5]
temp=arr[4]
arr[4]=arr[3]
arr[3]=arr[2]
arr[2]=arr[1]
arr[1]=arr[0]
arr[0]=temp
print(arr)