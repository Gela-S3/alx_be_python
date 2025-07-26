def perform_operation(num1, num2, operation):
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0 :
            print("Numbers can not be divided by 0")
        else :
            return num1 / num2
    else :
        print("Please choose correct word for the operation!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation =  input("Enter the operation (add, subtract, multiply, divide):").strip().lower()

result = perform_operation(num1, num2, operation)
print(result)