##import sys
##a=[1,2,3]
##count=sys.getrefcount(a)#reference count-it tracks the number of references
##print(count)
##
##a=[]
##b=a
##c=b
##print(sys.getrefcount(c))

##import gc
##collected=gc.collect()
##print("Garbage collected:",collected)
##
##import gc # garbage collector
##gc.enable()
##gc.disable()
##
##l1=[1,2,3]
##d1={'a':1,'b':2}
##s1="Garbage collection"
##del l1
##del d1
##del s1
###gc.set_threshold(1,2,2)
##print("current threshold is :",gc.get_threshold())
##collected=gc.collect()
##print(f"Garbage collector collected {collected} objects")

n=input("Enter a string:")
a=0
num =0
s =0
for i in n:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        num+=1
    else:
        s+=1

print("Alphabetic Characters:", a)
print("Numeric Characters:", num)
print("Special Characters:", s)
import re
def check(st):
    ex=r'^(?=.*[a-zA-Z])(?=.*[!@#$%^&*(){}\[\]:;\"\'<>,.?/\\|`~\-=_+]).+$'
    if re.match(ex,st):
        print("The string contains both alphabets and special characters.")
    else:
        print("The string must contain at least one alphabet and one special character.")
st=input("Enter your string:")
check(st)







