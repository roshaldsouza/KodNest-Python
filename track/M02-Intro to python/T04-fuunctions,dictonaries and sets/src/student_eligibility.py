def check_eligibility(marks, attendance, project_completed):
    # Check whether all three eligibility conditions are satisfied
    if marks >= 60 and attendance >= 75 and project_completed.lower() == "yes":
        return "Eligible"
    else:
        return "Not Eligible"

# Read the student's details
marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

# Call the function and print the returned result
result = check_eligibility(marks, attendance, project_completed)
print(result)
