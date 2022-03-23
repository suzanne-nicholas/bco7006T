class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#print(x.firstname)

#create a child class

class Student(Person):
    pass

y = Student("Harry", "Smith")
y.printname()

class Student(Person):
    super(). __init__(fname, lname)
    self.gradua