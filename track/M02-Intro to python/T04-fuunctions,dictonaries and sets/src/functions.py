def add_student(name, students=[]):
    # Add each name using append()
    students.append(name)
    # Print the list inside the function
    print(students)

# Read three student names from user input
first_name = input()
second_name = input()
third_name = input()

# Call the function three times without passing a list
add_student(first_name)
add_student(second_name)
add_student(third_name)
