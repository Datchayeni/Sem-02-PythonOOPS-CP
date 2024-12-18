"""class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
name=input("Enter your name:")
age=int(input("Enter your age:"))
std=Students(name,age)
n=input("Enter your another name:")
std.set_name(n)
print(f"Name:{std.get_name()}\nAge:{std.get_age()}")"""


class User:
    def __init__(self, username, password):
        self._username = username
        self.set_password(password)  
    def set_password(self, password):
        """Set the password after validation."""
        if len(password) < 8:
            print("Error: Password must be at least 8 characters long.")
            return
        if not any(char.isdigit() for char in password):
            print("Error: Password must contain at least one number.")
            return
        if not any(char in "!@#$%^&*()-_=+[{]};:'\",<.>/?`~" for char in password):
            print("Error: Password must contain at least one special character.")
            return
        self._password = password
        print("Password set successfully!")
    def check_password(self, input_password):
        """Verify if the input password matches."""
        if input_password == self._password:
            print("Password is correct!")
            return True
        else:
            print("Password is incorrect!")
            return False
user = User("JohnDoe", "Secure@123")  
user.check_password("Secure@123")


class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self.set_price(price)  
        self.set_stock(stock)  
    def set_price(self, price):
        if price > 0:
            self._price = price
            print("Price set successfully!")
        else:
            print("Error: Price must be greater than 0.")
            self._price = None
    def set_stock(self, stock):
        if isinstance(stock, int) and stock >= 0:
            self._stock = stock
            print("Stock set successfully!")
        else:
            print("Error: Stock must be a non-negative integer.")
            self._stock = None
    def get_stock(self):
        return self._stock
    def display_product(self):
        print(f"Product Name: {self._name}")
        print(f"Price: {self._price}")
        print(f"Stock: {self._stock} units")
product = Product("Laptop", 1200, 10)
product.display_product()
product.set_price(-500) 
product.set_stock(-5)
print("Current Stock:", product.get_stock())

class Student:
    def __init__(self, name, age, marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_age(self, age):
        if not 5 <= age <= 100:
            raise ValueError("Age must be between 5 and 100")
        self.__age = age
    def get_age(self):
        return self.__age
    def set_marks(self, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks
    def get_marks(self):
        return self.__marks
try:
    student = Student("Alice", 20, 85)
    print("Name:", student.get_name())
    print("Age:", student.get_age())
    print("Marks:", student.get_marks())
except ValueError as e:
    print(e)









