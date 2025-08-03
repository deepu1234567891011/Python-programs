class student:
    def __init__(self,name,id,branch):
        self.name=name
        self.id=id
        self.branch=branch
    def display_info(self):
        print("Student name is:",self.name)
        print("student id is:",self.id)
        print("student branch is:",self.branch)
    @staticmethod
    def show():
        print("--------WELCOME TO TH SCHOOL SYSTEM THIS IS PART OF STUDENTS-----------")
class teacher:
    def __init__(self,name,id,subject,salary):
        self.name=name
        self.id=id
        self.subject=subject
        self.salary=salary
    def display_info(self):
        print("Teacher name is:",self.name)
        print("Teacher id is:",self.id)
        print("Teacher subject is:",self.subject)
        print("Teacher salary is:",self.salary)
    @staticmethod
    def show():
        print("---------Welcome to the Teachers information part of school system---------")
# User input
student.show()
name = input("Enter student name: ")
id = input("Enter student ID: ")
branch = input("Enter student branch: ")
students = student(name, id, branch)

teacher.show()
name = (input("Enter teacher name: "))
id = input("Enter teacher ID: ")
subject = input("Enter teacher subject: ")
salary = input("Enter teacher salary: ")
teachers = teacher(name, id, subject, salary)

# Display info
students.display_info()
teachers.display_info()