#operator overloding
class Books:
    def __init__ (self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Books(150)
b2=Books(250)
print(b1+b2)

#method overloading
class add:
    def ad(self,a,b,c=0):
        result=0
        result=a+b+c
        return result
a=add()
ans=a.ad(2,3)
print(ans)
ans1=a.ad(22,10)
print(ans1)
