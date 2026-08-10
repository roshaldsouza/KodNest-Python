# Define the calculate function accepting two numbers and an arithmetic operator
def calculate(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    else:
        return first_number / second_number

# Read input values
first_number = int(input())
second_number = int(input())
operator = input().strip()

# Call function and store returned result
result = calculate(first_number, second_number, operator)

# Print the calculation result
print(result)
