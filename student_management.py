import json


# Load student records from the JSON file
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save student records to the JSON file
def save_students(students):
    try:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("File error! Data could not be saved.")


# Add a new student
def add_student():
    try:
        student = {
            "id": int(input("Enter ID: ")),
            "name": input("Enter name: "),
            "age": int(input("Enter age: ")),
            "course": input("Enter course: "),
            "marks": float(input("Enter marks: "))
        }

        students = load_students()

        if any(s["id"] == student["id"] for s in students):
            print("Student ID already exists!")
            return

        students.append(student)
        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Enter valid numeric values!")


# Display all students
def view_students():
    students = load_students()

    if not students:
        print("No students found!")
        return

    for s in students:
        print(f"\nID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print(f"Marks: {s['marks']}")


# Search for a student by ID
def search_student():
    try:
        id = int(input("Enter student ID: "))

        for s in load_students():
            if s["id"] == id:
                print("\nStudent found!")
                print(s)
                return

        print("Student not found!")

    except ValueError:
        print("Enter a valid ID!")


# Update an existing student
def update_student():
    try:
        students = load_students()
        id = int(input("Enter student ID: "))

        for s in students:
            if s["id"] == id:
                s["name"] = input("Enter new name: ")
                s["age"] = int(input("Enter new age: "))
                s["course"] = input("Enter new course: ")
                s["marks"] = float(input("Enter new marks: "))

                save_students(students)
                print("Student updated successfully!")
                return

        print("Student not found!")

    except ValueError:
        print("Enter valid numeric values!")


# Delete a student by ID
def delete_student():
    try:
        students = load_students()
        id = int(input("Enter student ID: "))

        for s in students:
            if s["id"] == id:
                students.remove(s)
                save_students(students)
                print("Student deleted successfully!")
                return

        print("Student not found!")

    except ValueError:
        print("Enter a valid ID!")


# Main menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")