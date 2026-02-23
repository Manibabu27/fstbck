from fastapi import APIRouter, Depends, HTTPException, params
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from db import get_db
from schemas import employe_details, attendance


router = APIRouter()

@router.post("/employees_details/")
async def create_employee(employee: list[dict], db: Session = Depends(get_db)):
    try:
        for emp in employee:
            new_employee = employe_details(**emp)
            db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/employees_details/")
async def get_employees(employe_id: int,db: Session = Depends(get_db)):
    try:
        employees = db.query(employe_details).filter(employe_details.employee_id == employe_id).all()
        return employees
    except Exception as e:
        raise   HTTPException(status_code=500, detail=str(e))
    
@router.delete("/employees_details/")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        employee = db.query(employe_details).filter(employe_details.employee_id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
        db.delete(employee)
        db.commit()
        return {"message": f"Employee with id {employee_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/attendance/")
async def create_attendance(attendance_data: dict, db: Session = Depends(get_db)):
    try:
        employee_id = attendance_data.get("employee_id")
        if employee_id is None:
            raise HTTPException(status_code=400, detail="employee_id is required")

        # Check if an employee with the given ID exists.
        employee = db.query(employe_details).filter(employe_details.employee_id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")

        new_attendance = attendance(**attendance_data)
        db.add(new_attendance)
        db.commit()
        db.refresh(new_attendance)
        return new_attendance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/attendance/")
async def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    try:
        attendance_records = db.query(attendance).filter(attendance.employee_id == employee_id).all()
        return attendance_records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
