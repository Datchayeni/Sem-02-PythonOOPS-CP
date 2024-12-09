"""class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def show(self):
        print("Vehicle Name:",self.name)
        print("Model:",self.model)
class Car(Vehicle):
    def __init__(self,name,model,brand):
        super().__init__(name,model)
        self.brand=brand
    def dis(self):
        print("Car Brand:",self.brand)
class Truck(Vehicle):
    def __init__(self,name,model,t_brand):
        super().__init__(name,model)
        self.t_brand=t_brand
    def disp(self):
        print("Truck Brand:",t_brand)
class Sportscar(Car,Vehicle):
    def __init__(self, name, model, brand, max_speed):
        super().__init__(name, model, brand)
        Vehicle.__init__(self,name,model)
        self.max_speed = max_speed
    def car_info(self):
        self.show()
        self.dis()
        print("Max Speed:", self.max_speed)
sportscar = Sportscar("Ferrari", "F8 Tributo", "Ferrari", "340 km/h")
sportscar.car_info()"""

class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def show(self):
        print("Name:",self.name)
        print("Marks")
        print("English:",self.mark1)
        print("Tamil:",self.mark2)
        print("Maths:",self.mark3)
class Percentage(Student):
    def cal(self):
        tot=self.mark1+self.mark2+self.mark3
        per=(tot/300)*100
        print("Total:",tot)
        print("Percentage:",per)
std=Percentage("Alice",70,50,60)
std.show()
std.cal()









        
