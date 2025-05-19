from abc import ABC, abstractmethod

# Base Abstract class for Person
class Person(ABC):
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        self.__age = value

    @abstractmethod
    def display_details(self):
        pass

# Student class inherits Person
class Student(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.courses = []

    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_details(self):
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.courses:
            print("Courses:")
            for c in self.courses:
                print(f" - {c.course_code}: {c.course_name}")
        else:
            print("No courses registered.")
        print("-"*30)

# Instructor class inherits Person
class Instructor(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.assigned_courses = []

    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)

    def display_details(self):
        print(f"Instructor ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.assigned_courses:
            print("Assigned Courses:")
            for c in self.assigned_courses:
                print(f" - {c.course_code}: {c.course_name}")
        else:
            print("No courses assigned.")
        print("-"*30)

# Course class
class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display(self):
        print(f"{self.course_code}: {self.course_name} ({self.credits} credits)")

# University Management System
class UniversitySystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def add_student(self):
        try:
            id = int(input("Enter Student ID: "))
            if any(s.id == id for s in self.students):
                print("Student ID already exists.")
                return
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            self.students.append(Student(id, name, age))
            print("Student added.")
        except ValueError:
            print("Invalid input.")

    def add_instructor(self):
        try:
            id = int(input("Enter Instructor ID: "))
            if any(i.id == id for i in self.instructors):
                print("Instructor ID already exists.")
                return
            name = input("Enter Instructor Name: ")
            age = int(input("Enter Instructor Age: "))
            self.instructors.append(Instructor(id, name, age))
            print("Instructor added.")
        except ValueError:
            print("Invalid input.")

    def add_course(self):
        code = input("Enter Course Code: ").upper()
        if any(c.course_code == code for c in self.courses):
            print("Course already exists.")
            return
        name = input("Enter Course Name: ")
        try:
            credits = int(input("Enter Credits: "))
            self.courses.append(Course(code, name, credits))
            print("Course added.")
        except ValueError:
            print("Invalid credits value.")

    def find_student(self, id):
        return next((s for s in self.students if s.id == id), None)

    def find_instructor(self, id):
        return next((i for i in self.instructors if i.id == id), None)

    def find_course(self, code):
        return next((c for c in self.courses if c.course_code == code), None)

    def register_student_course(self):
        try:
            sid = int(input("Enter Student ID: "))
            student = self.find_student(sid)
            if not student:
                print("Student not found.")
                return
            code = input("Enter Course Code: ").upper()
            course = self.find_course(code)
            if not course:
                print("Course not found.")
                return
            student.register_course(course)
            print("Course registered.")
        except ValueError:
            print("Invalid input.")

    def assign_instructor_course(self):
        try:
            iid = int(input("Enter Instructor ID: "))
            instructor = self.find_instructor(iid)
            if not instructor:
                print("Instructor not found.")
                return
            code = input("Enter Course Code: ").upper()
            course = self.find_course(code)
            if not course:
                print("Course not found.")
                return
            instructor.assign_course(course)
            print("Course assigned.")
        except ValueError:
            print("Invalid input.")

    def show_students(self):
        for s in self.students:
            s.display_details()

    def show_instructors(self):
        for i in self.instructors:
            i.display_details()

    def show_courses(self):
        for c in self.courses:
            c.display()

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. Add Instructor")
            print("3. Add Course")
            print("4. Register Student to Course")
            print("5. Assign Course to Instructor")
            print("6. Show Students")
            print("7. Show Instructors")
            print("8. Show Courses")
            print("0. Exit")
            choice = input("Choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_instructor()
            elif choice == '3':
                self.add_course()
            elif choice == '4':
                self.register_student_course()
            elif choice == '5':
                self.assign_instructor_course()
            elif choice == '6':
                self.show_students()
            elif choice == '7':
                self.show_instructors()
            elif choice == '8':
                self.show_courses()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    system = UniversitySystem()
    system.run()

print("Developed By Aqsa Majeed")
