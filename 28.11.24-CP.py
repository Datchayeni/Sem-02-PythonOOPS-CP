class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.sal=int(input("Enter the Salary:"))
    def displayInfo(self):
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()

class Inventory:
    def __init__(self,product_name,product_id,product_count):
        self.product_name=product_name
        self.product_id=product_id
        self.product_count=product_count
    def show(self):
        print("product name:",self.product_name)
        print("product Id:",self.product_id)
        print("product count:",self.product_count)
pro=Inventory("lipblam",234,8)
pro.show()


class Inventory:
    def __init__(self):
        self.product_name=input("Enter the product name:")
        self.product_id=input("Enter the product Id:")
        self.product_count=int(input("Enter the product count:"))
class Display(Inventory):
    def show(self):
        print("product name:",self.product_name)
        print("product Id:",self.product_id)
        print("product count:",self.product_count)
d=Display()
d.show()

    
