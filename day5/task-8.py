class Publisher:
    title_name ="John Carter"
    def display_publisher(self):
        print(f"Name : {self.title_name}")
class book(Publisher):
    no_pages = 200
    def display_book(self):
        print(f"Name : {self.title_name}")
        print(f'Pages: {self.no_pages}')

class tape(Publisher):
    time = 3
    def display_tape(self):
        print(f"Name : {self.title_name}")
        print(f'time :{self.time} hrs')

obj1 = book()
obj2 = tape()
print("----Publisher display()----")
obj1.display_publisher()
print("----Book display()----")
obj1.display_book()
print("----Tape display()----")
obj2.display_tape()