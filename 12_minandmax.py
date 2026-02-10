arr=[34,45,13,3545,67]
max=arr[0]
min=arr[0]
for i in arr:
    if(i>max):
       max=i
    if(i<min):
        min = i
print("maximum =", max)
print("minimum =", min)
