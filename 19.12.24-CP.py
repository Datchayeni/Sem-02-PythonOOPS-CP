##st=input("Enter a sentence:")
##def upperlower(st):
##    u=0
##    l=0
##    for i in st:
##        if i.isupper():
##            u+=1
##        elif i.islower():
##            l+=1
##    print("Upper Case:",u)
##    print("Lower Case:",l)
##upperlower(st)
##
##a=int(input("Enter subject 1 marks:"))
##b=int(input("Enter subject 2 marks:"))
##c=int(input("Enter subject 3 marks:"))
##d=int(input("Enter subject 4 marks:"))
##e=int(input("Enter subject 5 marks:"))
##tot=a+b+c+d+e
##per=(tot/500)*100
##print("Total=",tot)
##print("Percentage",per,"%")
##if per>=80:
##    print("Grade A")
##elif per>=70:
##    print("Grade B")
##elif per>=60:
##    print("Grade C")
##elif per>=40:
##    print("Grade D")
##else:
##    print("Grade E")


##import re
##word="Simple regular expression example regular"
##result=re.findall("gula",word)
##print(result)
##
##space=re.research("\s",word)
##print("\n The first space is at",space.start())


##class RomanConverter:
##    def int_to_roman(self, num):
##        roman_map = [
##            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
##            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
##            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
##        ]
##        result = ""
##        for value, symbol in roman_map:
##            while num >= value:
##                result += symbol
##                num -= value
##        return result
##converter = RomanConverter()
##number = int(input("Enter a number (1-3999): "))
##print(f"Roman numeral: {converter.int_to_roman(number)}")


#another method
##roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
##n=int(input("Enter the number to convert:"))
##ans=''
##for val,letter in roman:
##    while n>=val:
##        ans+=letter
##        n-=val
##print("The roman value for the given integer is:",ans)


##roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
##n=input("Enter the roman number to convert:")
##ans=0
##for val,letter in roman:
##    while n.startswith(letter):
##        ans+=val
##        perfix.remove(n)
##print("The roman value for the given integer is:",ans)


##import re
##def verify_password(password):
##    ex=r'^(?=.*[a-z A-Z]\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
##    if re.match(ex,password):
##        print("password is a strong")
##.    else:
##        print("password is not a strong")
##
##
##
##
##password=input("Enter the password:")
##verify_password(password)
##



##import re
##n=input()
##def verify(n):
##    ex=r'^(?=.*[a-z])(?=[{3,}A-Z])(?!.*[!@#$%^&*(),.?":{}|<>]).{12}$'
##    if re.match(ex,n):
##        print("valid")
##    else:
##        print("Invalid")
##verify(n)


import re
import random
class Member:
    def __init__(self, mem_id, name, email):
        self.mem_id = mem_id
        self.name = name
        self.email = email
    def verify_email(self):
        ex = r'^[a-z0-9._%+-]+@gmail\.com$'
        if re.match(ex, self.email, re.IGNORECASE):
            print("Valid email id")
        else:
            print("Invalid email id")
    def verify_number(self):
        id = r'^LIB\d{4}$'
        if re.match(id, self.mem_id):
            print("Valid member id")
        else:
            self.generate_id()
   def generate_id(self):
       self.mem_id = "LIB" + str(random.randint(1000, 9999))
       print("Generated new member id:", self.mem_id)
class Library(Member):
 def __init__(self, mem_id, name, email, book_id, title, author):
 super().__init__(mem_id, name, email)
 self.book_id = book_id
 self.title = title
 self.author = author
def display(self):
 print("Member id : ", self.mem_id)
 print("Name : ", self.name)
 print("Email : ", self.email)
 print("Book id : ", self.book_id)
 print("Title : ", self.title)
 print("Author : ", self.author)
 mem_id = input("Enter the member id : ")
 name = input("Enter the name : ")
 email = input("Enter the email : ")
 book_id = input("Enter the book id : ")
 title = input("Enter the title : ")
 author = input("Enter the author : ")
 lib = Library(mem_id, name, email, book_id, title, author)
 lib.verify_email()
 lib.verify_number()
 lib.display()




































    
