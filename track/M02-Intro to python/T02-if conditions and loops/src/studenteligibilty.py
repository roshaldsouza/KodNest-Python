Marks = int(input())
attendance = int(input())
project_status = input()
if Marks >= 60 and attendance >= 75:
    if project_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")