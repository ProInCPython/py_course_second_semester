import statistics

student = {"name" : "John", "age" : 19, "course" : 2, "grades" : [4, 5, 3, 2, 5, 4, 5, 3, 4, 5]}

print(f"Имя: {student.get("name")}, курс: {student.get("course")}")
print(statistics.mean(student.get("grades")))
student.get("grades").append(5)
print(student)