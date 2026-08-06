n = int(input())

positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for _ in range(n):
    num = int(input())
    total += num
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)
