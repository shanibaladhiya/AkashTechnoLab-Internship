class Employee:
    name ="Shani"
    designation ="Web Developer"
    def display(self):
        print(f"name : {self.name}\ndesignation : {self.designation}")

class Subclass(Employee):
    salary=10000
    def display_from_sub(self):
        print(f"name : {self.name}\ndesignation : {self.designation}\nSalary : {self.salary}")


obj1 = Subclass()
print('-------Employee class display()-------')
obj1.display()
print("-------Subclass display()---------")
obj1.display_from_sub()