a = input()

answer = ""
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in a:
    if lower.find(i) != -1:
        answer += lower[(lower.index(i) + 3) % 26]
    elif upper.find(i) != -1:
        answer += upper[(upper.index(i) + 3) % 26]
    else:
        answer += i
print(answer)