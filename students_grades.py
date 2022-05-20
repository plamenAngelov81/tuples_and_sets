n = int(input())

student_grades = {}
for i in range(n):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    grade_2f = " ".join(f'{grade:.2f}' for grade in grades)
    print(f"{student} -> {''.join(grade_2f)} (avg: {average_grade:.2f})")
