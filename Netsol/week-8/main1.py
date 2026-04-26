from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Student API", version="1.0")

students = [
    {"id": 1, "name": "Ali", "grade": "A"},
    {"id": 2, "name": "Sara", "grade": "B"},
]

class StudentCreate(BaseModel):
    name: str
    grade: Optional[str] = "N/A"

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    grade: Optional[str] = None

@app.get("/students")
def get_all_students():
    return students

@app.get("/students/{student_id}")
def get_one_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", status_code=201)
def add_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "grade": student.grade
    }
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, update: StudentUpdate):
    for student in students:
        if student["id"] == student_id:
            if update.name is not None:
                student["name"] = update.name
            if update.grade is not None:
                student["grade"] = update.grade
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(i)
            return {"message": f"Student {student_id} deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
