# Define the check_sign function to determine if a number is positive, negative, or zero
def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Read one integer input
number = int(input())

# Call check_sign function and store returned result
result = check_sign(number)

# Print the result
print(result)
