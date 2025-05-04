from datetime import date

class Person:
    
    rise_rate = 1.2
    person_number = 0

    def __init__(self,_name, _age):
        self.name = _name
        self.age = _age
        Person.person_number +=1

    def show_info(self):
        print(f"Name: {self.name} Age: {self.age}")

    # class method
    @classmethod
    def total_personal_number(cls):
        print("Total Personal Number : ",cls.person_number)

    @classmethod
    def create_with_string(cls,_str):
        name,age = _str.split("-")
        return cls(name,age)
    
    @classmethod
    def create_with_birth(cls,name,birth_year):
        return cls(name, date.today().year - birth_year)
    
    @staticmethod
    def birth_year(person):
        print(f"Name: {person.name} Birth Year: {date.today().year - person.age}")

p1 =  Person("James",26)
p2 = Person("Susan",27)

p3 = Person.create_with_string("Veli-36")
p3.show_info()

p4 = Person.create_with_birth("Mehmet",1996)
p4.show_info()

Person.birth_year(p2)

Person.total_personal_number()


    