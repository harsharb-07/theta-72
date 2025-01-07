students = {
    1: {"name": "Harsha", "marks": 20},
    2: {"name": "Nikki", "marks": 22},
    3: {"name": "Swetha", "marks": 16},
    4: {"name": "Michael", "marks": 21},
    5: {"name": "Vaishu", "marks": 5}, 
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name:{details['name']}, Marks: {details['marks']}")