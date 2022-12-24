array=list(map(int,input("array: ").split(",")))
target=int(input("target: "))
count=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==target:
            count.append(i)
            count.append(j)
print(count)