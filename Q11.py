sentences=input("sentences: ").split(",")
counts=[]
for i in sentences:
    count=0
    for j in i.split():
        count+=1
    counts.append(count)
print(max(counts))
