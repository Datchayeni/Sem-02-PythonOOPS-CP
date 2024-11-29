class Employee:
    def __init__(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position
    def show(self):
        print(f"name:{self.name}\nID:{self.id}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddress(self):
        print(f"Street name:{self.street}\nState name:{self.state}\nCountry name:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,id,position,street,state,country):
        super().__init__(name,id,position)#to call method
        Address.__init__(self,street,state,country)#to call method
    def displayEmp(self):
        self.displayaddress()
        self.show()
ed=EmployeeDetails("jiya",100,"manager","shenoy nagar","Tamilnadu",'India')
ed.displayEmp()




