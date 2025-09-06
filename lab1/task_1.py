class Student:

    def __init__(self, name : str, group : str, grades : list):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        if self.average_grade() >= 4.5:
            return True
        return False

f = open("students.txt", "r")
data = f.readlines()
students = [Student(i.strip().split(";")[0], i.strip().split(";")[1], list(map(int, i.strip().split(";")[2].split(",")))) for i in data]
f.close()

f = open("excellent_students.txt", "w")


for i in students:
    if i.is_excellent():
        f.write(f"{i.name} - {i.group}\n")
f.close()

ans = {}

for i in students:
    if ans.get(i.group) is None:
        ans.setdefault(i.group, i.grades)
    else:
        ans[i.group].extend(i.grades)

for j in ans.keys():
    print(j, round(sum(ans.get(j)) / len(ans.get(j)), 2))



