# abstraction and encapsulation

class library_system(object):
    max_numb_of_books = 20
    employees = 5
    wall_color = "green"

    def __init__(self):
        self.collection = ["To know", "Dont know", "This is", "You mean"]

    def view_books(self):
        return (print(self.collection))

    def check_out(self, book):
        for i in self.collection:
            if i == book:
                self.collection.remove(book)
                return
        return (print("%s is not in the collection"%book))

    def check_in(self, book):
        if book not in self.collection:
            self.collection.append(book)
        return(print("%s is aleady in the system"%book))


library = library_system()

library.view_books()
library.check_out("To know")
library.view_books()
