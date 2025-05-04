class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self): # Magic/Dunder method
        return f"Employee({self.first_name}, {self.last_name}, {self.pay})"

    def __str__(self): # Magic/Dunder method
        return f"{self.fullname()} - {self.email}"
    
    def __len__(self): # Magic/Dunder method
        return len(self.fullname())

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    
    @property 
    def email(self): 
        return f"{self.first_name}.{self.last_name}@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    @classmethod # it will be effecting all object's raise amount
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee): # inheritance
    raise_amount = 1.10 

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay) # or Employee.__init(self, first_name, last_name, pay)
        self.prog_lang = prog_lang

class Manager(Employee): # inheritance
    raise_amount = 1.50

    def __init__(self, first_name, last_name, pay, employess = None):
        super().__init__(first_name, last_name, pay)
        if employess is None:
            self.employess = []
        else:
            self.employess = employess

    def add_employee(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def show_employess(self):
        for emp in self.employess:
            print("---> ",emp.fullname()) 

emp_1 = Employee("John", "Wall", 4000)

dev_1 = Developer("Kobe", "Bryant",  5000, "Python")
dev_2 = Developer("Nikola", "Tesla", 6000, "Java")

manager_1 = Manager("Michael", "Jordan", 7000)

emp_1.fullname = "Alper Seyman"

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

# print(repr(emp_1)) # or emp_1.__rerpr__()
# print(str(emp_1)) # or emp_1.__str__()
# print(len(emp_1)) # or emp_1.__len__()
