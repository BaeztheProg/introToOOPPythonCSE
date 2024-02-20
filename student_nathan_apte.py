class Student:
    def __init__(self, first_name: str, last_name: str, id: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.arrival_time = None

        if isinstance(id, int):
            pass
        else:
            raise TypeError(f"{self.id} must be set to an instance of int!")

def register_new_student():
    print("Welcome new student!")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    student_id = None

    while not isinstance(student_id, int):
        student_id = "Enter your student ID (must be a unique integer): "

    return Student(first_name, last_name, student_id)

def take_attendance():
    student_id = input("Enter your user ID: ")
    
    for student in roster:
        if student_id == student.student_id:
            print("You're here")
            return False
        
        else:
            print("Student not found")
            return True

roster = []

is_taking_attendance = True

while is_taking_attendance:
    if take_attendance():
        roster.append(register_new_student())
