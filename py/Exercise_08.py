grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95),
]

students = set()
subjects = set()

for name, subject, grade in grades:
    students.add(name)
    subjects.add(subject)

print("Unique students:", students)
print("Unique subjects:", subjects)

print("All grades:")
for name, subject, grade in grades:
    print(name, "-", subject, "-", grade)

print("Average grade per student:")
for student in students:
    total = 0
    count = 0
    for name, subject, grade in grades:
        if name == student:
            total = total + grade
            count = count + 1
    average = total / count
    print(student, ":", average)

print("Average grade per subject:")
for subject in subjects:
    total = 0
    count = 0
    for name, s, grade in grades:
        if s == subject:
            total = total + grade
            count = count + 1
    average = total / count
    print(subject, ":", average)