class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def speak(self):
        print("Hello")
    
    def walk(self):
        print("walking away")
    
    def get_name(self):
        return self.fname + " " + self.lname
    
    def get_age(self):
        return self.age
    
# person = Person("Nana", "Obeng", 50)
# person_name = person.get_name()
# person_age = person.get_age()
# reply = person.walk()
# 
# print(f"Name: {person_name}")
# print(f"Age: {person_age}")
# print(reply)
    
class Student(Person):
    def __init__(self, fname, lname, age, courses):
        Person.__init__(self, fname, lname, age)
        self.courses = courses
    
    def get_courses(self):
        return self.courses
    
    def speak(self):
        print("I'm so tired")
    
student = Student("Nana", "Obeng", 50, "biology")
person_name = student.get_name()
person_age = student.get_age()
student_courses = student.get_courses()
reply = student.speak()

print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"Course(s): {student_courses}")
print(reply)