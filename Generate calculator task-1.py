# Designing a calculator with arithmetic operations
# input of two numbers based on operation choice

def calculation():
    # User input the two numbers
    global op_symbol, result
    # Prompt the user operations
    print("----------------------------------")
    print(" Choose the operation:")
    print("\t 1. Addition (+)")
    print("\t 2. Subtraction (-)")
    print("\t 3. Multiplication (*)")
    print("\t 4. Division (/)")
    print("----------------------------------")

    while True:
        choice = input("Enter choice(1/2/3/4): ")
        # Perform the Calculation based on the operation

        if choice == '1':
            num1 = float(input("Enter a First Number :"))
            num2 = float(input("Enter a Second Number :"))
            result = num1 + num2
            op_symbol = '+'

        elif choice == '2':
            num1 = float(input("Enter a First Number :"))
            num2 = float(input("Enter a Second Number :"))
            result = num1 - num2
            op_symbol = '-'

        elif choice == '3':
            num1 = float(input("Enter a First Number :"))
            num2 = float(input("Enter a Second Number :"))
            result = num1 * num2
            op_symbol = '*'

        elif choice == '4':
            num1 = float(input("Enter a First Number :"))
            num2 = float(input("Enter a Second Number :"))
            if num2==0:
                print("Error! Division by zero is not allowed. Try again ...")
                continue
            else:
                result = num1 / num2
                op_symbol = '/'

        else:
            print("Invalid operation. Please select 1, 2, 3, or 4.")
            continue # Skip the display if the operation is invalid

        # Display the result
        print("\n** Display the result **")
        print(f"\t{num1} {op_symbol} {num2} = {result}")
        print("----------------------------------")

        # Check if user wants another calculation
        next_cal = input("Do you want a another calculation?(yes/no): ")
        if next_cal.lower() == 'no':
            break

    print("\n\tTHANKS FOR USING...!!!")


#MAIN PROGRAM
calculation()




