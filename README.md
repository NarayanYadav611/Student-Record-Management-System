# Student Record Management System

## Project Description

Student Record Management System is a console-based Python application used to manage student records efficiently.

The application allows users to add, view, search, update, and delete student records. Student data is stored in a JSON file so that the records remain available even after the program is closed.

## Features

* Add new student records
* View all student records
* Search student by ID
* Update student information
* Delete student records
* Prevent duplicate student IDs
* Store data permanently using JSON
* Handle invalid user input using exception handling
* Simple menu-driven console interface

## Technologies Used

* Python
* JSON
* File Handling
* Exception Handling

## Python Concepts Used

* Variables and Data Types
* Lists and Dictionaries
* Conditional Statements
* Loops
* Functions
* Exception Handling
* File Input/Output
* JSON Data Handling
* Menu-driven Programming

## Student Record Fields

Each student record contains:

* Student ID
* Name
* Age
* Course
* Marks

## Project Structure

```text
Student-Record-Management-System/
│
├── student_management.py
├── students.json
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python student_management.py
```

5. The application menu will appear in the terminal.

## Menu Options

```text
===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

## Sample Record

```text
ID: 1
Name: Rahul
Age: 21
Course: MCA
Marks: 85.0
```

## Data Storage

Student records are stored in `students.json`.

The program uses:

* `json.load()` to read records
* `json.dump()` to save records

## Exception Handling

The application handles common errors such as:

* Invalid numeric input
* Invalid student ID
* Missing JSON file
* Invalid JSON data
* File saving errors

This prevents the program from terminating unexpectedly during normal user input errors.

## Future Enhancements

* Add student sorting
* Add marks/grade calculation
* Add graphical user interface
* Add database connectivity using MySQL
* Add login/authentication
* Generate student reports

## Conclusion

The Student Record Management System demonstrates the practical use of Python programming concepts such as functions, loops, conditional statements, exception handling, and file handling.

It provides a simple and effective way to manage student records through a console-based interface.
