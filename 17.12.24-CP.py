"""class Library:
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"

class DigitalLibrary(Library):
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"

lib=Library()
dig=DigitalLibrary()

book=input()
username=input()

print(lib.issue_book(book,username))
print(lib.return_book(book,username))

print(dig.issue_book(book,username))
print(dig.return_book(book,username))"""


class Library:
    def __init__(self):
        self.book_name="The Cruel Prince"
        self.user="Datchayeni"
    def issue_book(self):
        return f"Book issued : {self.book_name} to {self.user}"
    def return_book(self):
        return f"Book returned : {self.book_name} by {self.user}"

class DigitalLibrary(Library):
    def __init__(self,book_name,user):
        self.book_name=book_name
        self.user=user
    def issue_book(self):
        return f"Book issued : {self.book_name} to {self.user}"
    def return_book(self):
        return f"Book returned : {self.book_name} by {self.user}"
book=input()
username=input()

lib=Library()
dig=DigitalLibrary(book,username)

print(lib.issue_book())
print(lib.return_book())

print(dig.issue_book())
print(dig.return_book())



