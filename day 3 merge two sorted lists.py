n=int(input("enter the number of n: "))
a=[]
for i in range(n):
    a.append(int(input("enter the element: ")))
n1=int(input("enter the number of n1: "))
b=[]
for i in range(n1):
    b.append(int(input("enter the element: ")))
c=[]
c=a+b
print("list=",c)
c=list(set(c))
print("sorted=",c[ : :-1])
