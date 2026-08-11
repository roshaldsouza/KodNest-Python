# Read the number of registration entries
n = int(input())

# Create an empty set to store unique student IDs
registrations = set()

# Read and store the student IDs
for _ in range(n):
    student_id = input().strip()

    # Add the student ID to the set
    registrations.add(student_id)

# Read the student ID to search
search_id = input().strip()

# Calculate the number of unique registrations
unique_count = len(registrations)

# Calculate the number of duplicate entries
duplicate_count = n - unique_count

# Output the results
print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

# Check if the search ID exists in the set
if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")
