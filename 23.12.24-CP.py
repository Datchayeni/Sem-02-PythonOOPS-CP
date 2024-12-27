#3
n=int(input("Enter a number:"))
n=str(n)
c=0
for i in n:
    i=int(i)
    c+=i
print("Sum of digits:",c)

#4
l1=list(map(int,input("Enter a list:").split(",")))
l2=list(map(int,input("Enter a list:").split(",")))
if len(l1)==len(l2):
    l1=set(l1)
    l2=set(l2)
    merge=l1&l2
    print("The merged list is:",list(merge))
else:
    print("The lenght of the list should be equal:")

#5
s=input("Enter a string:")
count=0
for j in s:
    if j.isspace():
        count+=1
print("The total words in the string:",count)

6
l=list(map(int,input("Enter a list:").split(",")))
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list is:",l)

#7
class BankAccount:
    def __init__(self,acc_holder_name,balance):
        self.acc_holder_name=acc_holder_name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(amount,"Rupees deposited successfully. Balance:",self.balance,"Rupees")
    def withdraw(self,amount):
        if amount>0:
            if amount<self.balance:
                self.balance-=amount
                print(amount,"Rupees withdrawn successfully. Balance:",self.balance,"Rupees")
    def check(self):
        print("Account Balance:",self.balance,"Rupees")
acc=BankAccount("Alice",5000)
acc.check()
acc.deposit(7000)
acc.withdraw(2000)

#8
import re
def check_email(email):
    ex=r'^[a-z A-Z 0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(ex,email):
        print("Valid")
    else:
        print("Invalid")
email=input("Enter your email:")
check_email(email)

#9
s=input("Enter a sentence:")
c=""
for i in s:
    if i.isdigit():
        c+=i
print(c)

#10
st=input("Enter a sentence:")
s=""
for j in st:
    if j!="#":
        s+=j
print(s)

#2
lst=list(map(int,input("Enter a list:").split(",")))
print(lst)
lst=set(lst)
l=list(lst)
l.sort(reverse=True)
print(l)



















