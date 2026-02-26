from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, params
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from db import get_db
from schemas import employe_details, attendance


router = APIRouter()

@router.post("/employees_details/")
async def create_employee(employee: dict, db: Session = Depends(get_db)):
    eid = employee.get("employee_id")
    if not eid:
        raise HTTPException(status_code=400, detail="employee_id is required")
    if not str(eid).isdigit():
        raise HTTPException(status_code=400, detail="Please enter a number for employee_id")  
    
    existing_employee = db.query(employe_details).filter(employe_details.employee_id == eid).first()
    if existing_employee is not None:
        raise HTTPException(status_code=400, detail=f"Employee with id {eid} already exists")
    
    try:
       
        new_employee = employe_details(**employee)
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/employees_details/")
async def get_employees(db: Session = Depends(get_db)):
    try:
        employees = db.query(employe_details).all()
        return employees
    except Exception as e:
        db.rollback()
        raise   HTTPException(status_code=500, detail=str(e))
    
@router.delete("/employees_details/")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(employe_details).filter(employe_details.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    try:
        employee = db.query(employe_details).filter(employe_details.employee_id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
        db.delete(employee)
        db.commit()
        return {"message": f"Employee with id {employee_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/attendance/")
async def create_attendance(attendance_data: dict, db: Session = Depends(get_db)):
    employee_id = attendance_data.get("employee_id")
    employee_date = attendance_data.get("date")
    if employee_id is None:
        raise HTTPException(status_code=400, detail="employee_id is required")

    # Check if an employee with the given ID exists.
    employee = db.query(employe_details).filter(employe_details.employee_id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    existing_attendance = db.query(attendance).filter(
            attendance.employee_id == employee_id,
            attendance.date == employee_date
        ).first()
    if existing_attendance:
            raise HTTPException(status_code=400, detail=f"Attendance for employee with id {employee_id} on date {employee_date} already exists")
    employee_date = datetime.strptime(employee_date, "%Y-%m-%d")
    if employee_date > datetime.now():
        raise HTTPException(status_code=400, detail=f"Attendance date {employee_date} is in the future Date")
    try:
        
        new_attendance = attendance(**attendance_data)
        db.add(new_attendance)
        db.commit()
        db.refresh(new_attendance)
        return new_attendance
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/attendance/")
async def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    try:
        attendance_records = db.query(attendance).filter(attendance.employee_id == employee_id).all()
        return attendance_records
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
