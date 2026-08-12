class StudentProfile:
    def __init__(self,student_id,name,course,score,skills,is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = [] if skills is None else list(skills)
        self.is_placed = is_placed
    def __str__(self):
        skills_text = (", ".join(self.skills) if self.skills else "Not Added")
        placement_text = ("Placed" if self.is_placed else "Not Placed")
        return (f"{self.student_id} | {self.name} | {self.course} | {self.score} | {self.skills_text} | {self.placement_text}")
student = StudentProfile(student_id = 101,name = "Rahul", course = "Python", score = 78,is_placed = True)
print(student)
        
