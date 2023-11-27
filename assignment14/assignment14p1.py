def calculate():
    try:
        expression = input('Please enter expression \npress exit to stop the function: ')
        if (expression == 'exit'):
            return
        # Split the input expression into numbers and operator
        args = expression.split(' ')
        
        # Check if the expression has the correct format
        if len(args) != 3:
            raise ValueError("Invalid expression format. Please use the format: number operator number")

        # Convert the numbers to floats
        num1 = float(args[0])
        num2 = float(args[2])
        
        # Perform the operation based on the operator
        if args[1] == '+':
            result = num1 + num2
        elif args[1] == '-':
            result = num1 - num2
        elif args[1] == '*':
            result = num1 * num2
        elif args[1] == '/':
            # Check for division by zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Supported operators are +, -, *, /")

        # Print the result
        print(f"{args[0]} {args[1]} {args[2]} = {result}")



    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    calculate()

calculate()