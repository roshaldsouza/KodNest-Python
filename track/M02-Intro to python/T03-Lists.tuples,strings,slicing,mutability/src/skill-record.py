# 1. Initialize an empty list to store five skills
skills = []

# Read five skill inputs from the user and append them to the list
for i in range(5):
    skill = input()
    skills.append(skill)

# 2. Convert the list into a tuple named skill_record
skill_record = tuple(skills)

# 3. Use tuple slicing to display required slices
print("Skill Record:", skill_record)               # Original tuple containing all 5 skills
print("First Three:", skill_record[:3])            # Slices first 3 elements (indices 0, 1, 2)
print("Last Two:", skill_record[-2:])              # Slices last 2 elements (indices -2, -1)
print("Alternate Skills:", skill_record[::2])       # Slices every 2nd element starting from index 0
print("Reversed Skills:", skill_record[::-1])      # Reverses the tuple using step of -1
