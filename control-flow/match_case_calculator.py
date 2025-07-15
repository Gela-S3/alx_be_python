num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
match operation:
    case '+':
        print(f"The result is {sum}.")
    case '-' :
        print(f"The result is {subtraction}.")
    case '*' :
        print(f"The result is {multiplication}.")
    case '/':
        if num2 == 0 :
            print("Cannot divide by zero.")
        else :
            division = num1/num2
            print(f"The result is {division}.")