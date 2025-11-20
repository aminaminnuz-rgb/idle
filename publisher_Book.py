class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        if hasattr(self, "publisher"):
            print(f"{self.title} written by {self.author} published by {self.publisher}")
        else:
            print("Unknown publisher")

b1 = Book("python","john")
b1.publisher = "TechPress" 
b1.info()

b2 = Book("abc","xyz")
b2.info()

