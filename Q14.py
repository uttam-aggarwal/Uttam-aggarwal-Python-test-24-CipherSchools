list1=list(map(int,input("list: ").split(",")))
final_list=[]
for i in list1:
    final_list.append(tuple([i,i**3]))
print(final_list)