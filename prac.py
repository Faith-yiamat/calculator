

print("select option")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
     a = input("enter first number:")
     b = input("enter second number:")
     print("sum is: " + str(int(a) +int(b)))


elif operation =="2":
    a= input("enter first number:")
    b= input("enter second number:")
    print("difference is: " + str(int(a) - int(b)))
elif operation == "3":
    a= input("enter first number: ")
    b= input("enter second number; ")
    print("multiple: " + str(int(a)* int(b)))
elif operation == "4":
    a= input("enter first number: ")
    b = input("enter second number:")
    print("division: " + str (int(a) /int(b)))
