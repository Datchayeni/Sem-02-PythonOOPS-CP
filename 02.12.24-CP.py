class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id=",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age,Id)
        self.Salary=Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary=",self.Salary)
man=Manager("Datchayeni",17,2613,10000)
man.displayManager()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name =", self.name, "\nAge =", self.age)
class Employee(Person):
    def __init__(self, name, age, Id):
        super().__init__(name, age)
        self.Id = Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id =", self.Id)
class Manager(Person):
    def __init__(self, name, age, Salary):
        super().__init__(name, age)
        self.Salary = Salary
    def displayManager(self):
        self.displayPerson()
        print("Salary =", self.Salary)
emp = Employee("Datchayeni", 17, 2613)
emp.displayEmployee()
man = Manager("Poongu", 18, 10000)
man.displayManager()




















