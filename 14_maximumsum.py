arr=[2,3,-8,7,-1,2,3]
sum = arr[0]
maxsum =arr[0]
start=0
end=0
newstart=0
for i in range (1,len(arr)):
    if sum+arr[i]<arr[i]:
        sum=arr[i]
        newstart=i
    else:
        sum=sum+arr[i]
    if sum>maxsum:
        maxsum=sum
        start=newstart
        end=i
print("maximum sum=",maxsum)
print("sub array=",arr[start:end+1])                