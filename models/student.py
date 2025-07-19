from init import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Student(db.Model):
# Name of the table

#Attributes
id = db.Column(db.Interger, primary_key = True)
name = db.Column(db.String(100), nullanble = False)
email = db.Column(db.String(100), nullable = False, unique = True)
address = db.Column(db.String(100))

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

# Student Schema for converting a single entry
student_schema = StudentSchema()

#Student Schema for converting multiple entrie
students_schema = StudentSchema(many=True)