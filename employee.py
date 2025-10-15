class Employee:
    def __init__(self, name, age):
        self.name = name      # public
        self._age = age       # protected 

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)

emp = SubEmployee("Ross", 21)
print(emp.name)
emp.show_age()
