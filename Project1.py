'''Project: Student Management System

Build a console-based program where you can manage students.

What your program should do

When the program starts:

===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Calculate Grade
5. Show Topper
6. Remove Student
7. Exit

Enter your choice:
'''


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def info(self):
        return f" Name:{self.name}\n Roll-No.:{self.roll_no}\n Marks:{self.marks}"


students = []

# Showing Student


def show_student():
    for each_student in students:
        print(each_student.info())
        print("\n")

# Adding Student


def add_student():
    duplicate = False
    name = input("Name:")
    roll = int(input("Roll-no:"))
    marks = int(input("Marks:"))
    for each_student in students:
        if each_student.roll_no == roll:
            duplicate = True
            print("stop")
            break
    if duplicate == True:
        print("Student Already Exists")
    else:
        new_student = Student(name, roll, marks)
        print("Students added successfully!!")
        return new_student

# Search Student


def searchStudent():
    searhing_roll = int((input("\n Enter the roll no.:")))
    count = 0
    for each_student in students:
        if each_student.roll_no == searhing_roll:
            print("Student Found!!")
            print(each_student.info())
        else:
            count += 1
    if count == len(students):
        print("Student Not Found.")

# Calculate Grade


def calculate_grade():
    count = 0
    Roll_for_Grade = int(input("\n Enter the Roll No.:"))
    for each_student in students:
        if each_student.roll_no == Roll_for_Grade:
            marks = each_student.marks
            if marks >= 90 and marks <= 100:
                Grade = 'A+'
            elif marks >= 80 and marks < 90:
                Grade = 'A'
            elif marks >= 70 and marks < 80:
                Grade = 'B'
            elif marks >= 60 and marks < 70:
                Grade = 'C'
            elif marks >= 50 and marks < 60:
                Grade = 'D'
            else:
                Grade = 'F'
            print(f"{each_student.info()}\n Grade: {Grade}")
        else:
            count += 1
    if count == len(students):
        print("Student Not Found.")

# Show Topper


def topper():
    t_mark = 0
    if len(students) == 0:
        print("Add Student! No student found!!!")
    else:
        for each_student in students:
            marks = each_student.marks
            if marks > t_mark:
                t_mark = marks
                t_info = each_student
        print(t_info.info())


# Remove Student

def Remove_student():
    count = 0
    to_remove = int(input("Enter the roll to remove Student:"))
    for each_student in students:
        if to_remove == each_student.roll_no:
            students.remove(each_student)
            print("---Student Removed---")
            removed = each_student.info()
            print(removed)
        else:
            count += 1
    if count == len(students):
        print("Student not found!!!")

# Manu


while True:
    print('''===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Calculate Grade
5. Show Topper
6. Remove Student
7. Exit

''')
    user = int(input("Enter Your choice:"))
    if user == 1:
        new_student = add_student()
        if new_student != None:
            students.append(new_student)
    elif user == 2:
        show_student()
    elif user == 3:
        searchStudent()
    elif user == 4:
        calculate_grade()
    elif user == 5:
        topper()
    elif user == 6:
        Remove_student()
    elif user == 7:
        print("Thanks To Use!!!")
        break
    else:
        print("Plz Enter under the choice: ")
