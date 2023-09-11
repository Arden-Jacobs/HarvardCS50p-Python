# File Name: student13.py

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script then demonstrates creating a student instance and prints it without implementing the '__str__' method.

# Define the 'Student' class with a constructor (__init__) to represent a student.
class Student:
    def __init__(self, name, house):
        # Validate the 'name' to ensure it's not empty.
        if not name:
            raise ValueError("Missing name")
        
        # Validate the 'house' to ensure it's one of the valid options.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        # If both 'name' and 'house' pass validation, initialize the 'name' and 'house' attributes of the 'Student' instance.
        self.name = name
        self.house = house

# Define the main function.
def main():
    # Call the 'get_student' function to collect the student's information and create an instance of the 'Student' class directly.
    student = get_student()
    
    # Print the 'student' instance directly.
    print(student)

# Define the 'get_student' function to collect the student's information and create an instance of the 'Student' class directly.
def get_student():
    # Collect the student's name and house using the 'input' function.
    name = input("Name: ")
    house = input("House: ")
    
    # Create an instance of the 'Student' class directly and pass the collected information as arguments to its constructor.
    return Student(name, house)

# Check if the script is run as the main program.
if __name__ == "__main__":
    # If it is, call the 'main' function to create a student instance, collect input, and print the student instance directly.
    main()

# Explanation:

# Description: This script defines a class 'Student' with a constructor (__init__) to represent a student with 'name' and 'house' attributes.
# It adds validation checks within the constructor to ensure that the 'name' is not empty and the 'house' is one of the valid options.
# The script then demonstrates creating a student instance and prints it without implementing the '__str__' method.

# The script consists of the following components:

# - 'Student' class: This class is defined with a constructor (__init__) that takes two parameters, 'name' and 'house'. Inside the constructor,
#   there are two validation checks:
#   - The 'name' is validated to ensure it's not empty. If it is, a 'ValueError' is raised with the message "Missing name."
#   - The 'house' is validated to ensure it's one of the valid options: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin. If it's not one of
#     these options, a 'ValueError' is raised with the message "Invalid house." If both 'name' and 'house' pass validation, the 'name' and 'house'
#     attributes of the 'Student' instance are initialized with the provided values.

# - 'main': This function is the entry point of the script. It calls the 'get_student' function to collect the student's information and create
#   an instance of the 'Student' class directly. It then prints the 'student' instance directly. However, since the 'Student' class does not
#   have a '__str__' method defined, the default string representation of the 'student' instance will be printed.

# - 'get_student': This function is responsible for collecting the student's name and house using the 'input' function. It then creates an instance
#   of the 'Student' class directly by calling its constructor and passing the collected information as arguments. The function returns the 'Student'
#   instance directly, eliminating the need for an intermediate variable.

# The script also checks whether it is executed as the main program. If it is, it initiates the interactive process by calling the 'main' function,
# allowing the user to input the student's name and house and demonstrating how to create and print a student instance without implementing a
# custom '__str__' method.
