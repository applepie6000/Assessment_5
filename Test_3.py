class Person:
    def __init__(self,first_name,last_name,age,Location):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
        self.Location = Location
    def display(self):
        print(f"{self.first_name} {self.last_name} is currently {self.age} years old and lives in {self.Location}" )


person1 = Person("Erick","Smith",30,"Kenya")
person2 = Person("James","Cooper",43,"Kenya")
person3 = Person("Alex", "Kamau",23,"Kenya")
print(person1.display())


class Student(Person):
    def __init__(self,first_name,last_name,age,Location,School,Grade):
        super().__init__(first_name,last_name,age,Location)
        self.School = School
        self.Grade = Grade
    def display_1(self):
        print(f"{self.first_name} {self.last_name} is currently {self.age} years old and lives in {self.Location} where he goes to {self.School} and had a Grade of {self.Grade}")

student1 = Student("Jack","Mathew", 18,"Kenya","M-pesa High School","A-")
student2 = Student("Kenny","Israel", 19,"Kenya","M-pesa High School",'A')
student3 = Student("June", 'Ann', 18,'Kenya','M-pesa High School','a')



print(student1.display_1())

class Employee(Person):
    def __init__(self,first_name,last_name,age,Location,Work,Period):
        super().__init__(first_name,last_name,age,Location)
        self.Work = Work
        self.Period = Period
    def display_2(self):
        print(f"{self.first_name} {self.last_name} is currently {self.age} years old and lives in {self.Location} where he goes to work at {self.Work} and has been working there for the last {self.Period} years.")

employee1 = Employee("John", "Peter", 23,"Kenya","Safaricom","Ten")
employee2 = Employee("Alvin","John",34,"Kenya","Safaricom","Sixteen")
employee3 = Employee("Simon","John",35,"Kenya","Safaricom","Twenty one")

print(employee1.display_2())


