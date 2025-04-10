class StudentDataBase:
    __student_list = []
    
    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)
    
    @classmethod
    def get_student_by_id(cls, student_id):
        for student in cls.__student_list:
            if student_id == student.get_student_id():
                return student
        return None
    
    @classmethod
    def remove_student(cls, student_id):
        student = cls.get_student_by_id(student_id)
        if student:
            cls.__student_list.remove(student)
            return True
        return False
    
    @classmethod
    def view_all_students(cls):
        if not cls.__student_list:
            print("No students in the database")
        else:
            for student in cls.__student_list:
                student.view_student_info()
                print("-" * 30)

class Student:
    def __init__(self, student_id, name, department, is_enrolled=True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDataBase.add_student(self)
    
    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_department(self):
        return self.__department
    
    def is_enrolled(self):
        return self.__is_enrolled
    
    def view_student_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Status: {'Enrolled' if self.__is_enrolled else 'Not Enrolled'}")

def menu():
 
    Student("S001", "Alice Johnson", "Computer Science")
    Student("S002", "Bob Smith", "Electrical Engineering")
    
    while True:
        print("\nStudent Database Management System")
        print("1. View All Students")
        print("2. Enroll New Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nAll Students:")
            StudentDataBase.view_all_students()
        
        elif choice == "2":
            print("\nEnroll New Student")
            try:
                student_id = input("Enter student ID: ").strip()
                if StudentDataBase.get_student_by_id(student_id):
                    print(f"Error: Student with ID {student_id} already exists!")
                    continue
                
                name = input("Enter student name: ").strip()
                department = input("Enter department: ").strip()
                
                
                Student(student_id, name, department)
                print(f"\nSuccessfully enrolled {name} ({student_id}) in {department}")
            
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("\nDrop Student")
            student_id = input("Enter student ID to drop: ").strip()
            if StudentDataBase.remove_student(student_id):
                print(f"Student {student_id} has been dropped from the School")
            else:
                print(f"Error: Student with ID {student_id} not found")
        
        elif choice == "4":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-4")

if __name__ == "__main__":
    menu()
