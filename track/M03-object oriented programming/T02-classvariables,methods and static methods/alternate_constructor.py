class StudentProfile:
    def __init__(self, student_id, name, course, experience):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience

    # Create the from_text() alternative constructor
    @classmethod
    def from_text(cls, data):
        student_id, name, course, experience = data.split("|")
        return cls(int(student_id), name, course, int(experience))


data = input().strip()

# Create the StudentProfile object using from_text()
student = StudentProfile.from_text(data)

# Print the stored profile
print("Student ID:", student.student_id)
print("Name:", student.name)
print("Course:", student.course)
print("Experience:", student.experience, "years")
