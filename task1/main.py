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

@app.get("/students/{name}")
async def get_student(name: str):
    for student in students:
        if student.name == name:
            return student.to_dict()
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/students/")
async def get_students():
    return [student.to_dict() for student in students]

async def save_students():
    data = [student.to_dict() for student in students]
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


