# Read three integer scores and store them in original_scores
original_scores = []
for _ in range(3):
    original_scores.append(int(input()))

# Create alias_scores by referencing original_scores (creates an alias, not a copy)
alias_scores = original_scores

# Read replacement score and additional score
replacement_score = int(input())
additional_score = int(input())

# Modify the shared list through alias_scores
alias_scores[0] = replacement_score
alias_scores.append(additional_score)

# Display both variables and check whether they refer to the same object in memory
print("Original:", original_scores)
print("Alias:", alias_scores)
print("Shared Object:", original_scores is alias_scores)
