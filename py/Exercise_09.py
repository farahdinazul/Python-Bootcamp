student_records = {
    "students" : {
        "student_001": {"name":"John", "age":"19", "major":"Computer Science", "grades":"[85,92,78]"},
        "student_002": {"name": "Sarah", "age":"20", "major": "Biology", "grades": "[90, 88, 95]"}
    }
}

print(student_records["students"].items())

#2
student_records["student_003"] = {"name":"Mike", "age":"18", "major": "Math", "grades" : "[82,79,91]"}
print(student_records["students"].items())