print("Welcome guys and hello everyone")
from random import randint
print(f'The random number is {randint(0,100)}')
mylist=[1,2,3,4,5]
for i in mylist :
    if(i%2!=0) :
        pass
    else:
        print(f'it is even {i}')
i=0
while i<len(mylist):
    if(mylist[i]%2==0):
        print('it is even')
    else:
        pass
    i+=1
print(range(0,100))

def sum_of_nums(a,b):
    return a+b
print(sum_of_nums(10,20.0))
print('new from today')