class Staff:
    def __init__(self,first_name,last_name,age,duty):
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.duty= duty
class Teacher(Staff):
    def __init__(self,first_name,last_name,age,duty,subject):
        super().__init__(first_name,last_name, age, duty)
        self.subject= subject
    def display(self):
        print(f"{self.first_name} {self.last_name} is currently at the age of  {self.age} and has the duty of {self.duty} and is in charge of the {self.subject} department")

teacher1= Teacher('Erick','Smith',30,'Teacher','Mathmatics')
teacher2= Teacher('Marry','Jane',23,'Teacher','English')
teacher3= Teacher('Kelvin','Stone',22,'Teacher','Biologhy')

print(teacher1.display())
class Cook(Staff):
    def __init__(self,first_name,last_name,age,duty,kitchen):
        super().__init__(first_name,last_name,age,duty)
        self.kitchen= kitchen
    def display(self):
        print(f"{self.first_name} {self.last_name} is currently at the age of  {self.age} and has the duty of {self.duty} and works in the {self.kitchen} kitchen.")\

cook1= Cook('Ann','Kamau',30,'Cook','Students')
cook2= Cook('John','Njoroge',43,'Cook','Teachers')
cook3= Cook('Jane','Njoroge',23,'Cook','Students')

print(cook1.display())






