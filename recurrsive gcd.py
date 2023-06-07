def gcd(n1,n2):
    if n2==0:
        return n1
    else:
        return gcd(n2, n1%n2)

n1=int(input('enter first number'))
n2=int(input('enter second number'))

n=gcd(n1,n2)
print(n)