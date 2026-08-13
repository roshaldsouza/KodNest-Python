# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    # Read the student details
    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    # Filter and display the matching students
    def filter_students_by_course(self, course):
        matches = []
        for student in self.student_profiles:
            if student.course.lower() == course.lower():
                matches.append(student)
        return matches


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

required_course = input().strip()
results = manager.filter_students_by_course(required_course)

if results:
    for student in results:
        print(student)
else:
    print(f"No students found for course: {required_course}")