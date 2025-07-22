from init import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Student(db.Model):
    # Name of the table
    # __tablename__ = "students"
    
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100))

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

# Student Schema for converting a single entry
student_schema = StudentSchema()

# Student Schema for converting multiple entries
students_schema = StudentSchema(many=True)