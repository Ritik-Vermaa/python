n = int(input("Enter a number n: "))

prime = True
i = 2
while i <= n/2:
        if n % i == 0:
            prime = False
            break
        i += 1

if prime:
        print("Number is prime")
else:
        print("Number is not prime")
