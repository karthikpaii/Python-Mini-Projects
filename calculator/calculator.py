try:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    print("Choose calculation to Perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    cal = input("Enter choice (add/subtract/multiply/divide): ").strip().lower()

    if cal == "add":
        ans = num1 + num2
        print(ans)
    elif cal == "subtract":
        ans = num1 - num2
        print(ans)
    elif cal == "multiply":
        ans = num1 * num2
        print(ans)
    elif cal == "divide":
        if num2 == 0:
            print("Error: Cannot divide by zero")
            ans = None
        else:
            ans = num1 / num2
            print(ans)
    else:
        print("Invalid Operation")
        ans = None

 
except ValueError:
    print("Invalid Input! Please enter a valid number!")
