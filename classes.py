# classes.py
# Demonstrates a basic class with attributes and multiple objects


class Student:
    """A simple class representing a student."""

    def __init__(self, name, admission_number, course):
        # Instance variables - unique to each object
        self.name = name
        self.admission_number = admission_number
        self.course = course

    def display_info(self):
        """Prints the student's information."""
        print(f"Name: {self.name}")
        print(f"Admission Number: {self.admission_number}")
        print(f"Course: {self.course}")
        print("-" * 30)


# Creating three Student objects
student1 = Student("Mark Otieno", "CS/1234/2023", "Computer Science")
student2 = Student("Jane Wanjiru", "IT/5678/2023", "Information Technology")
student3 = Student("Peter Kimani", "CS/9012/2023", "Computer Science")

# Displaying information for each student object
print("--- Student Information ---")
student1.display_info()
student2.display_info()
student3.display_info()
