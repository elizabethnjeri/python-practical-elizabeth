# class_methods.py
# Demonstrates a constructor, instance variables, a class variable,
# and a class method using @classmethod


class Student:
    # Class variable - shared by all Student objects
    total_students = 0

    def __init__(self, name, course):
        # Instance variables - unique to each object
        self.name = name
        self.course = course

        # Increase the class variable every time a new student is created
        Student.total_students += 1

    def display_info(self):
        """Prints this student's details."""
        print(f"Name: {self.name}, Course: {self.course}")

    @classmethod
    def get_total_students(cls):
        """
        Class method - operates on the class itself (cls) rather than
        an individual instance (self). Used here to return the total
        number of Student objects created so far.
        """
        return cls.total_students

    @classmethod
    def create_default_student(cls):
        """
        Another example class method - acts as an alternative constructor
        that creates a Student object with default values.
        """
        return cls("Unnamed Student", "Undeclared")


# Creating Student objects using the normal constructor
student1 = Student("Mark Otieno", "Computer Science")
student2 = Student("Jane Wanjiru", "Information Technology")

student1.display_info()
student2.display_info()

# Using the class method to check the total number of students created
print("\nTotal students created:", Student.get_total_students())

# Creating a student using the alternative constructor class method
student3 = Student.create_default_student()
student3.display_info()

# The class variable updates again after the third student is created
print("Total students created after adding a default student:", Student.get_total_students())
