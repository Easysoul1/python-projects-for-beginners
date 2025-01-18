# Pratice Exercises
# Question 1 Week 9

file = open("./asset/textFile.txt", "r")
content = file.read()
try:
       word_count = len(content)
       line_count = content.count("\n") + 1
       char_count = len(content.split())
       print(f'The file has {word_count} words, {line_count} lines and {char_count} characters')
except FileNotFoundError:
       print('File not found')

finally:
       print('Done !')


file.close()

# Question 3 Week 9
# Creating a student database using JSON
import json

# Define the file name where student records will be stored
DATABASE_FILE = "students.json"


def load_students():
    try:

        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:

        return []


def save_students(students):
    with open(DATABASE_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(name, age, student_id):

    students = load_students()
    students.append({"name": name, "age": age, "student_id": student_id})
    save_students(students)
    print(f"Student {name} added successfully.")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, ID: {student['student_id']}")

def delete_student(student_id):
    students = load_students()
    students = [student for student in students if student["student_id"] != student_id]
    save_students(students)
    print(f"Student with ID {student_id} deleted successfully.")

def main():
    while True:
        # Display the menu options
        print("\nStudent Database")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student_id = input("Enter student ID: ")
            add_student(name, age, student_id)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

