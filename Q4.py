sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
new_keys=[]
for i in sample_dict.keys():
    if i=="city":new_keys.append("location")
    else:new_keys.append(i)
sample_dict=dict(zip(new_keys,list(sample_dict.values())))
print(sample_dict)