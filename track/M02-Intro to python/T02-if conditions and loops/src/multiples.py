limit = int(input())
target = int(input())

count = 0
total = 0
found = False
for i in range(1,limit):
    if i % 3 == 0:
        count += 1
        total = total + i
        if target == i:
            found =True
        else:
            found = False
print("Count: ",count)
print("Sum: ",total)

if found:
    print("Target found: Yes")
else:
    print("Target not found: no")
