class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Students=[]

n=int(input("How Much Student need to add : "))

for i in range(n):
    name=input(f"Enter Student Name {i+1}: ")
    age=int(input(f"Enter Student Age {i+1}: "))

    student = Student(name, age)
    Students.append(student)

print("\n Print List:")

for s in Students:
    print(f"Name: {s.name}, Age: {s.age}")





