def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input("enter a number"))
isPrime = check_prime(n)
if isPrime:
    print("number is prime")
else:
    print("number is not prime")

