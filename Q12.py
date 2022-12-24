string=input()
list1=[]
count_L,count_R=0,0
final_count=0
for i in string:
    if i=="L":count_L+=1
    elif i=="R":count_R+=1
    if count_L==count_R:
        final_count+=1
        count_L,count_R=0,0
print(final_count)