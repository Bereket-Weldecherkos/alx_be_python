def perform_operation(num1, num2, operation):
    # match operation:
    #     case "add":
    #         return num1 + num2
    #     case "subtract":
    #         return num1 - num2
    #     case "multiply":
    #         return num1 * num2
    #     case "divide":
    #         return num1 / num2 if num2 != 0 else "Division by zero error"
    #     case _:
    #         return "Invalid operation"
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero error"
        return num1 / num2
    else:
        return "Invalid operation"
    