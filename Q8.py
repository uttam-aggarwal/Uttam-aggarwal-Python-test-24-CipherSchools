array=list(map(int,input("array: ").split(",")))
new_array=[]
for i in array:
    if i<0:new_array.append(i)
for i in array:
    if i>0:new_array.append(i)
print(new_array)