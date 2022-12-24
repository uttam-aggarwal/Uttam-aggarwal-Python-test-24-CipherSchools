array=list(map(int,input("array: ").split(",")))
sum=int(input("sum: "))
count=0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==sum:count+=1
print(count)