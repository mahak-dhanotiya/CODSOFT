# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.


que = "Yes"

# Displaying user friendly message
print("Hello! Welcome")
print("CALCULATOR")

while (que.lower() == "yes"):
    # Taking input from user
    number1 = float(input("\nEnter first number: "))
    number2 = float(input("Enter second number: "))

    # Displaying Operations
    print("\nOptions are:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Floor Division (//)")
    print("7. Exit")

    # Enter operation choice
    operation_choice = int(input("Enter operation choice to be performed (1-7): "))

    # Perform the calculation
    if operation_choice == 1:
        result = number1 + number2
    elif operation_choice == 2:
        result = number1 - number2
    elif operation_choice == 3:
        result = number1 * number2
    elif operation_choice == 4:
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero"
    elif operation_choice == 5:
        if number2 != 0:
            result = number1 % number2
        else:
            result = "Error: Modulus by zero"
    elif operation_choice == 6:
        if number2 != 0:
            result = number1 // number2
        else:
            result = "Error: Floor division by zero"
    elif operation_choice == 7:
        print("Exiting calculator!!")
        break
    else:
        result = "Invalid choice"

    # Display result
    print("Result is:", result)
    
    # Choice to run again  
    que = input("Want to calculate more (Yes/No) ?")
    
print("OK! Bye!")

    





    
    