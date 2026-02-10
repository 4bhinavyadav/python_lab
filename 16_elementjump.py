arr=[1,3,5,8,9,2,6,7,6,8,9]
maxreach=arr[0]
stepleft=arr[0]
jumps=1
n=len(arr)
for i in range(1,n):
    if i==n-1:
        print(jumps)
        break
    maxreach=max(maxreach,i+arr[i])
    stepleft -=1
    if stepleft ==0:
        jumps +=1
        if i>=maxreach:
            print(-1)
            break
        stepleft = maxreach - i
                       
