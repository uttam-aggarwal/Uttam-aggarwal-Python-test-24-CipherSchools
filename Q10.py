array=list(map(int,input("array: ").split(",")))
new_array=[]
new_array.append(max(array))
array.remove(max(array))
new_array.append(max(array))
new_array.append(min(array))
array.remove(min(array))
new_array.append(min(array))
print((new_array[0]*new_array[1])-(new_array[-1]*new_array[-2]))