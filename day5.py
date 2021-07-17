#lambda function

x=[4,5,6,67,56,4,99,65]

def operate(a):
     c=[]
     for i in a:
          c.append(i*2)
     return c

def operate1(a):
     c=[]
     for i in a:
          c.append(i/10)
     return c
y=operate(x)
print(y)

y1=operate1(x)
print(y1)


#instead of making seperate two functions we will create one function using lambda functions
def operate2(f,a):
     c=[]
     for i in a:
          c.append(f(i))
     return c
          
y2=operate2(lambda n:n*2,x)
print(y2)

y3=operate2(lambda n:n/2,x)
print(y3)

y4=operate2(lambda n:'Even'if not n%2 else 'Odd',x)
print(y4)

#Map function
y5=list(map(lambda n:n%3,x))
print(y5)

#filter function
y6=list(filter(lambda n:n%2==1,x))
print(y6)

import myModule_day5
print(myModule_day5.message)

#Bare file Handling
f=open('sample3.txt','r')
r=f.read()
print(r)
f.close()

import json
f=open('sample2.json','r')
r=json.load(f)
print(r)






