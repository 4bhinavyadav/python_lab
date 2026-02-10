arr=[2,3,4]
target =6
def twosum(nums,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return[i,j]
    return[]
print(f"Result:{twosum([2,3,4],6)}")            
            