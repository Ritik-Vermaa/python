a = int(input("Enter Number a :"))


def printfact(a):
    fact = 1
    
    i=1
    while(i<=a):
        fact *= i
        i += 1
    
    
    print("The factorial is : " + str(fact)) 
    
printfact(a)    