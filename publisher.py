class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Book Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_pages = no_pages

    def display(self):
        super().display()
        print("Book Price:", self.price)
        print("Number of Pages:", self.no_pages)



p1 = Python("O'Reilly Media", "Learning Python", "Mark Lutz", 750, 1648)
p1.display()
