n = int(input("Enter number n : "))

i = 2

while i <= n:
    prime = True
    j = 2
    
    while j <= i // 2: 
        if i % j == 0:
            prime = False
            break
        j = j + 1
    
    if prime:
        print(i)
    
    i = i + 1
        
    
    

