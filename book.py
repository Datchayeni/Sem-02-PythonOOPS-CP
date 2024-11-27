class Books: 
    def __init__(self):
        self.bookname="The Cruel Prince"
        self.author="Holly Black"
    def show(self):
        print(f"Book Name:{self.bookname}",'\n',f"Author:{self.author}")      
book1=Books()
book1.show()

class Books:
    def __init__(self,bookname,author):
        self.bookname=bookname
        self.author=author
    def show(self):
        print(f"Book Name:{self.bookname}",'\n',f"Author:{self.author}")
book1=Books("The Midnight Library","Matt Haig")
book1.show()

class Books:
    def __init__(self,bookname="Haunting Adeline",author="H.D.Carlton"):
        self.bookname=bookname
        self.author=author
    def show(self):
        print(f"Book Name:{self.bookname}",'\n',f"Author:{self.author}")
book1=Books()
book1.show()


    
