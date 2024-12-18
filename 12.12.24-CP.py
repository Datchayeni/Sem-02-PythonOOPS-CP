# ticket booking application:
import random
class Customer:
    def __init__(self,cust_id,name,phno):
        self.cust_id=cust_id
        self.name=name
        self.phno=phno
    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customer_id(cust_id):
        if len(cust_id)==8:
            if cust_id[0:4]=="TICK" and cust_id[4:8].isdigit():
                print("valid")
            else:
                print("Invalid")
        else:
            print("ID should contain 8 characters")

class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":2000,"seats":50000},
                     "Movie":{"price":150,"seats":200},
                     "Match":{"price":1000,"seats":10000},}
        self.booked_tickets=[]
        
    def View_events():
        for events,details in self.events.items():
            print(f"{events}:{details['price']}per ticket{details['seats']}seats are available")
    def book_tickets():
        if event_name is self.events:
            event=self.events[event_name]
            if event["seats"]>=quantity:
                totalprice=["price"]*quantity
                event=["seats"]-= quantity
                self.bookes_tickets.append({"customer_id".customer.cust_id,"event",event_name,quantity})
            else:
                print("Seats are not available")
        else:
            print("Event name is not available")
    def view_tickets(self,customer):
        print("*******Tickets Informatin*******")
        cut_ticket=[t for t in self.book_tickets if t["customer"]]
                
        
        
        
    
            
        
        





book=TicketBooking()
print("*Welcome to TICKET booing appliction *******")
cust_id=input("Enter the customer id")

if Customer.verify_customer_id(cust_id):
    name=input("Enter your naame")
    phno=int(input("Enter your number"))
    cusomer=Customer(cust_id,name,phno)
    print("bookig details")
else:
    print("In valid!!!please register")
    name=input("Enter your name:")
    phno=int(input("Enter your number"))
    cust_id=self.gen_rand_id()
    cusomer=Customer(cust_id,name,phno)
    print("Your customer id is:",cust_id)

while True:
    print("Booking info")
    print("\n1. View Events")
    print("\n2. Book tickets")
    print("\n3. View my Tickets")
    print("\n4. Exit")
    choice=int(input("Enter any option to continue booking"))
    if choice==1:
        book.View_events()
    elif choice==2:
        event_name=input("Enter any evet:")
        quantity=int(input("Enter the number of tickets:"))








"""class Student:
    def __init__(self, name, std_id, grade):
        self.name = name
        self.std_id = std_id
        self.grade = grade

    def validate_id(self):
        if len(self.std_id) == 7 and self.std_id[0:3] == "STU" and self.std_id[3:].isdigit():
            return "Valid Student ID"
        else:
            return "Invalid Student ID. It must start with 'STU' and be followed by 4 digits (e.g., STU1234)."

    def validate_name(self):
        if len(self.name) >= 2 and all(char.isalpha() or char.isspace()
for char in self.name):
            return "Valid Name"
        else:
            return "Invalid Name. It must contain only alphabets and spaces and be at least 2 characters long."

    def validate_grade(self):
        for i in range (1,13):
            if i==1:
               f"{i}st Grade"
            elif i==2:
               f"{i}nd Grade"
            elif i==3:
               f"{i}rd Grade"
            else:
                f"{i}th Grade"
        if self.grade in self.validate_grade():
            return "Valid Grade"
        else:
            return "Invalid Grade. Grade must be between '1st Grade' and '12th Grade'."

    def display_details(self):
        print("Validating Student Details...")
        print(self.validate_id())
        print(self.validate_name())
        print(self.validate_grade())
        print("\nDisplaying Student Details:")
        if (
            self.validate_id() == "Valid Student ID"
            and self.validate_name() == "Valid Name"
            and self.validate_grade() == "Valid Grade"):
            print(f"Name: {self.name}")
            print(f"Student ID: {self.std_id}")
            print(f"Grade: {self.grade}")
        else:
            print("Some details are invalid. Please correct them and try again.")
student1 = Student("Alice Johnson", "STU1234", "1th Grade")
student1.display_details()

student2 = Student("Bob", "ST1234", "13th Grade")
student2.display_details()


def merge_strings(word1, word2):
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    merged.extend(word1[i:])
    merged.extend(word2[j:])
    
    return ''.join(merged)
word1 = input()
word2 = input()
st = merge_strings(word1, word2)
print(st)

def PlaceFlowers(flowerbed, n): 
    count = 0 
    for i in range(len(flowerbed)): 
         
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or 
flowerbed[i + 1] == 0): 
            flowerbed[i] = 1  
            count += 1   
            if count >= n:   
                return True 
    return count >= n 
flowerbed1 = [1, 0, 0, 0, 1] 
n1 = 1 
print(PlaceFlowers(flowerbed1, n1))   
flowerbed2 = [1, 0, 0, 0, 1] 
n2 = 2 
print(PlaceFlowers(flowerbed2, n2))"""















        
