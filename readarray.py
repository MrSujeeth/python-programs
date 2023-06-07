a=[]

n=int(input("enter a number"))
print("enter numbers")
for i in range(n):
    element=int(input())
    a.append(element)

print("elements of array are:",a)
print("1st elements of array are:",a[0])
print("3rd elements of array are:",a[2])
