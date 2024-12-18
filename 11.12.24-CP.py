"""class Student:
    _id=66876#private
    _course="AI"
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Student Name:",self.name)
s=Student("Alice")
s.display()
print(s._course)
print(s._id)

#name handling
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
emp=Employee("Jackson",50000)
print("Name:",emp.name)
print("Salary",emp._Employee__salary)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def dis(self):
        print("Name:",emp.name)
        print("Salary",emp._Employee__salary)
class Manager(Employee):
    def __init__(self,name,salary,emp_id):
        super().__init__(name,salary)
        self.emp_id=emp_id
    def show(self):
        self.dis()
        print("Employee ID:",self.emp_id)
emp=Manager("Alice",50000,"f67e7")
emp.show()"""


class PasswordValidator:
    def __init__(self, password):
        self.password = password
    def has_uppercase(self):
        if self.password[0].isupper():
            return True
        return False
    def has_lowercase(self):
        for char in self.password:
            if char.islower():
                return True
        return False
    def has_digit(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False
    def has_special_char(self):
        special_characters = "!@#$%^&*()-_=+[{]};:'\",<.>/?`~"
        for char in self.password:
            if char in special_characters:
                return True
        return False
    def is_min_length(self):
        return len(self.password) == 8
    def validate(self):
        uppercase = self.has_uppercase()
        lowercase = self.has_lowercase()
        digit = self.has_digit()
        special_char = self.has_special_char()
        min_length = self.is_min_length()
        print(f"Uppercase letter: {'Passed' if uppercase else 'Failed password`s first letter should be in capital'}")
        print(f"Lowercase letter: {'Passed' if lowercase else 'Failed'}")
        print(f"Digit: {'Passed' if digit else 'Failed'}")
        print(f"Special character: {'Passed' if special_char else 'Failed'}")
        print(f"Minimum length of 8 characters: {'Passed' if min_length else 'Failed'}")
        if uppercase and lowercase and digit and special_char and min_length:
            print("Password is Valid!")
        else:
            print("Password is Invalid!")
password = input("Enter your password: ")
validator = PasswordValidator(password)
validator.validate()


























