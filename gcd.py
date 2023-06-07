def get_gcd(a,b):
  gcd=1

  if a>b:
    temp=b
  else:
      temp=a
  for i in range(1,temp+1):
    if a % i==0 and b % i==0:
        gcd=i
  return gcd

n1=int(input('enter first number'))
n2=int(input('enter second number'))

print("gcd of",n1,"and",n2,"is",get_gcd(n1,n2))
