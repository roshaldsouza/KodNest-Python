class StudentProfile:
    def __init__(self, name, experience, skills):
        # Store the initial student data
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience):
        # Replace the current experience
        self.experience = new_experience

    def add_skill(self, new_skill):
        # Add the new skill to the existing list
        self.skills.append(new_skill)


# Read the student's initial data
name = input().strip()
experience = int(input())
skills = input().strip().split()

# Create one StudentProfile object
student = StudentProfile(name, experience, skills)

# Read the new experience and new skill
new_experience = int(input())
new_skill = input().strip()

# Call both update methods
student.update_experience(new_experience)
student.add_skill(new_skill)

# Print the updated student profile
print(f"Name: {student.name}")
print(f"Experience: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")
