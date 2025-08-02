from fastapi import FastAPI, HTTPException
import json
from student import Student

app = FastAPI()

students = []

try:
    with open("students.json", "r") as file:
        data = json.load(file)
        students = [Student.from_dict(student_dict) for student_dict in data]
except FileNotFoundError:
    pass

@app.post("/students/")
async def create_student(name: str, subject_scores: dict):
    student = Student(name, subject_scores)
    students.append(student)
    await save_students()
    return student.to_dict()

async def save_students():
    data = [student.to_dict() for student in students]
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


