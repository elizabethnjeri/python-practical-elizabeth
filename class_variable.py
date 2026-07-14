# class_variables.py
# Demonstrates the use of a class variable shared by all objects of a class


class Student:
    # Class variable - shared by ALL instances of this class
    school_name = "The Cooperative University of Kenya"

    def __init__(self, name, course):
        # Instance variables - unique to each object
        self.name = name
        self.course = course


# Creating multiple Student objects
student1 = Student("Mark Otieno", "Computer Science")
student2 = Student("Jane Wanjiru", "Information Technology")

# Accessing the class variable through different objects
print("Accessing class variable through student1:", student1.school_name)
print("Accessing class variable through student2:", student2.school_name)

# Accessing the class variable directly through the class itself
print("Accessing class variable through the class:", Student.school_name)

# Demonstrating that changing the class variable affects all objects
# (unless an instance variable with the same name overrides it)
Student.school_name = "Cooperative University - Main Campus"
print("\nAfter updating the class variable via the class:")
print("student1.school_name:", student1.school_name)
print("student2.school_name:", student2.school_name)

# If we set school_name on one instance only, it creates an INSTANCE
# variable for that object, which does not affect the others
student1.school_name = "Cooperative University - Nairobi Campus"
print("\nAfter setting school_name on student1 only (creates instance variable):")
print("student1.school_name:", student1.school_name)
print("student2.school_name:", student2.school_name)
