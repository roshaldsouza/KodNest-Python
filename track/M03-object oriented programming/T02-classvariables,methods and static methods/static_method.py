class StudentProfile:
    def __init__(self, name, experience):
        # Store the name and experience
        self.name = name
        self.experience = experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        if experience >= 0 and experience <= 40:
            return True
        else:
            return False


name = input().strip()
experience = int(input())

# Validate the experience using the class name
res = StudentProfile.is_valid_experience(experience)

# Create and print the profile only when valid
if res:
    student = StudentProfile(name, experience)
    print(f"Profile Created Name: {student.name} Experience: {student.experience} years")
else:
    print("Invalid Experience")
