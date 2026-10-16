students = []

# to check the grade of a student

def StudentGrade(grade):
    if grade>=85:
        print('Your grade is Excellent')
    elif grade>=75:
        print('Your grade is Very Good')
    elif grade>=65:
        print('Your grade is Good')
    elif grade>=60:
        print('You Passed')
    else:
        print('You Failed, Please try again')


def create_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    quiz_grade = int(input("Enter Quiz Grade: "))

    student = [student_id, name, quiz_grade]
    students.append(student)

    print("Student added successfully")
    StudentGrade(quiz_grade)  # Call the StudentGrade function to check the grade

def edit_student():
    student_id = input("Enter Student ID to edit: ")

    for student in students:
        if student[0] == student_id:
            student[1] = input("Enter new name: ")
            student[2] = int(input("Enter new quiz grade: "))
            StudentGrade(student[2])  # Call the StudentGrade function to check the grade

            print("Student updated successfully")
            return

    print("Student not found")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student[0] == student_id:
            students.remove(student)

            print("Student deleted successfully")
            return

    print("Student not found")


def display_students():
    for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Quiz Grade:", student[2])



# Add students
create_student()

# Display students
display_students()

# Edit a student
edit_student()

# Display after editing
display_students()

# Delete a student
delete_student()

# Display after deleting
display_students()
