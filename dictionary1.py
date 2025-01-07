students = {
    1: {"name": "google", "age": 20},
    2: {"name": "delloite", "age": 22},
    3: {"name": "pwc", "age": 19},
    4: {"name": "aaa", "age": 21},
    5: {"name": "Vaishu", "age": 5}, 
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name:{details['name']}, Age: {details['age']}")