# ==========================================
# 1. READ STUDENT COUNT & POPULATE MARKS LIST
# ==========================================
student_count = int(input())  # Reads total number of students
marks = []                    # Creates an empty list to hold the marks

# Loop 'student_count' times to collect each student's mark
for index in range(student_count):
    mark = int(input())       # Reads individual student's mark as integer
    marks.append(mark)        # Appends the mark to the end of the list

# ==========================================
# 2. READ CORRECTION & PASSING THRESHOLD
# ==========================================
position = int(input())        # Reads 1-based position of mark to update (e.g. 1st student = position 1)
corrected_mark = int(input())  # Reads the new corrected mark value
passing_mark = int(input())    # Reads the passing mark threshold

# ==========================================
# 3. UPDATE MARK IN LIST (LIST MUTABILITY)
# ==========================================
# Convert 1-based position to 0-based index (e.g. position 1 becomes index 0)
list_index = position - 1
marks[list_index] = corrected_mark  # Updates the specific item in the list

# ==========================================
# 4. CALCULATE STATISTICAL METRICS
# ==========================================
total_marks = sum(marks)                      # Calculates sum of all elements in the list
average_marks = total_marks / student_count  # Calculates average (total / total count)
highest_mark = max(marks)                     # Finds maximum value in the list
lowest_mark = min(marks)                      # Finds minimum value in the list

# ==========================================
# 5. COUNT PASSED STUDENTS
# ==========================================
passed_students = 0  # Counter variable initialized to 0

# Loop through each student mark in the list
for mark in marks:
    if mark >= passing_mark:
        passed_students += 1  # Increment counter if mark meets or exceeds passing mark

# ==========================================
# 6. DISPLAY RESULTS
# ==========================================
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Students: {passed_students}")
