array=[2,5,7,44,66,885,965,4,84,75,90]
peaks=[]
for i in range(len(array)):
    if i==0:
        if array[0]>array[1]:
            peaks.append(array[i])
    elif i==len(array)-1:
        if array[i]>array[i-1]:
            peaks.append(array[i])
    else:
        if array[i-1]<array[i]>array[i+1]:
            peaks.append(array[i])
print(peaks)