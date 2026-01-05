import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    email TEXT
)
""")
conn.commit()

# Step 3: Insert Student

def add_student(name, age, course, email):
    cursor.execute(
        "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
        (name, age, course, email)
    )
    conn.commit()
    print("Student added successfully")

# Step 4: View Students

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall() #returns all rows as a list.
    for row in data:
        print(row)

# Step 5: Update Student

def update_student(student_id, age):
    cursor.execute(
        "UPDATE students SET age = ? WHERE student_id = ?",
        (age, student_id)
    )
    conn.commit()
    print("Student updated")

# Step 6: Delete Student

def delete_student(student_id):
    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )
    conn.commit()
    print("Student deleted")

# Step 7: Main Program (Menu Driven)

while True:
#Runs continuously using while True.
    print("\n1.Add Student\n2.View Students\n3.Update Student\n4.Delete Student\n5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        email = input("Email: ")
        add_student(name, age, course, email)

    elif choice == "2":
        view_students()

    elif choice == "3":
        sid = int(input("Student ID: "))
        age = int(input("New Age: "))
        update_student(sid, age)

    elif choice == "4":
        sid = int(input("Student ID: "))
        delete_student(sid)

    elif choice == "5":
        break

    else:
        print("Invalid choice")

#Safely closes the database connection.
conn.close()