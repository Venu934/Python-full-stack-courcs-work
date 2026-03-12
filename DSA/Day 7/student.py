
student_name = ""
student_name = ""
def show_menu():
    print("\n----Attendance Tracker----")
    print("1. Add Attendance")
    print("2. View Attendance")
    print("3. Exit")
def add_attendance():
    global student_name
    student_name = input("Enter student name: ")
    student_status = input("Is the student present? (yes/no): ")
    print(f"Attendance added for {student_name}")
def view_attendance():
    if student_name:
        
