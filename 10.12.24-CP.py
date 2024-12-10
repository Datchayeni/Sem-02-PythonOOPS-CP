"""class Student:
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Department:",self.dept)
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def dis(self):
        print("Street:",self.street)
        print("State:",self.state)
        print("Country:",self.country)
class StudentInfo(Student,Address):
    def __init__(self,name,age,dept,street,state,country):
        Student.__init__(self,name,age,dept)
        Address.__init__(self,street,state,country)
    def info(self):
        print("Student Details")
        self.show()
        self.dis()
name=input("Enter your name:")
age=int(input("Enter your age:"))
dept=input("Enter your department:")
street=input("Enter your street:")
state=input("Enter your state:")
country=input("Enter your country:")
std=StudentInfo(name,age,dept,street,state,country)
std.info()"""

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
class Manager(Employee):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"ID: {self.ID}")

class Developer(Employee):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    def displayDeveloperInfo(self):
       
        print(f"Department: {self.dept}")


class TeamLeader(Manager, Developer):
    def __init__(self, name, age, ID, dept, teamsize):
        Employee.__init__(self, name, age)
        self.ID = ID
        self.dept = dept
        self.teamsize = teamsize
    def displayTeamInfo(self):
        self.displayEmployeeInfo()
        print(f"ID: {self.ID}")
        print(f"Department: {self.dept}")
        print(f"Team size: {self.teamsize}")


Name = input("Enter the name: ")
Age = int(input("Enter the age: "))
ID = int(input("Enter the ID: "))
Dept = input("Enter the department: ")
Teamsize = input("Enter the team size: ")
tl = TeamLeader(Name, Age, ID, Dept, Teamsize)
tl.displayTeamInfo()













        
