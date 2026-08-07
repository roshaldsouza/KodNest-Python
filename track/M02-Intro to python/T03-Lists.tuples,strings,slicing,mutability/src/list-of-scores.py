n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(scores)
search_score = int(input())

print("Highest Score:",max(scores))
print("Lowest Score:",min(scores))
print("Total number of scores:",len(scores))
if search_score in scores:
    print("Result Found")
else:
    print("Result not found")