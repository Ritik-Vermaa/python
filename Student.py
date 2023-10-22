
Math = int(input("Enter Math Marks: "))
Dsa = int(input("Enter Dsa Marks: "))
Python = int(input("Enter Python Marks: "))
Java = int(input("Enter Java Marks: "))
Php = int(input("Enter Php Marks: "))

Result =(Math + Dsa + Python + Java + Php)
avg = Result /5


if avg >= 65:
    print("First div")
    
elif avg >= 55 and avg < 65:
    print("Second div")
    
elif avg >= 45 and avg < 55:
    print("3rd div")
    
else:
    print("Fail")
