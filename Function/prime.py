a = int(input("Enter Number a : "))
prime = True

def printprime(a):
    i= 2
    while i>a:
         if a % i == 0:
            prime = False
            break
         i += 1
    
    
if prime :
        print("Number is prime")
else:
        print("Number is not prime")
        
        
        
        
printprime(a)        
            