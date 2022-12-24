def FizzBuzz(a):
    if a%3==0 and a%5==0:return "FizzBuzz"
    elif a%3==0:return "Fizz"
    elif a%5==0:return "Buzz"
    else:return a
n=int(input("number: "))
list1=[]
for i in range(1,n+1):
    list1.append(FizzBuzz(i))
print(list1)
