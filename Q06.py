array=list(map(int,input().split(",")))
k=int(input())
count=0
for i in range(len(array)):
    if count==k-1:
        print(min(array))
        break
    else:
        count+=1
        array.remove(min(array))