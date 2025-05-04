class Personal:
    rise_rate = 1.1
    def __init__(self,name, surname, age="No Info", salary="No Info"):
        self.name = name
        self.surname = surname
        self.age= age
        self.salary= salary
        self.email = name.lower() + surname.lower() + "@company.com"
    
    def show_info(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nSalary: {self.salary}")
    
    def show_mail(self):
        print(self.email)

class Software(Personal):
    rise_rate = 1.2
    def __init__(self,name, surname, language="No Info", age="No Info", salary="No Info"):
        super().__init__(name,surname,age,salary)
        self.language = language
    
    def show_info(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nSalary: {self.salary}\nLanguage: {self.language}")

class Manager(Personal):
    def __init__(self, name, surname, employeers=None, age="No Info", salary="No Info"):
        super().__init__(name, surname, age, salary)
        
        if employeers == None:
            self.employeers = []
        else:
            self.employeers = employeers
    
    def add_employeer(self,emp):  # emp = employeer
        if emp not in self.employeers:
            self.employeers.append(emp)
    
    def delete_employeer(self,emp):
        if emp  in self.employeers:
            self.employeers.remove(emp)

    def show_employeers(self):
        for emp in self.employeers:
            emp.show_info()
            print("****************")

s1 = Software("s1_name","s1_surname",language="Java",age=27,salary=5000)
s2 = Software("s2_name","s2_surname",language="C",age=26,salary=6000)

p1 = Personal("p1_name","p1_surname",age=25,salary=1500)
p2 = Personal("p2_name","p2_surname",age=32,salary=4000)

m1 = Manager("m1_name","m1_surmane",employeers=[s1,s2,p1,p2],age=45,salary=10000)

m1.show_employeers()