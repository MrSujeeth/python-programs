
num=int(input("enter the number"))
num_copy=num

rev=0
while num!=0:
    rem=num % 10
    rev=(rev*10)+rem
    num //=10

if num_copy==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")