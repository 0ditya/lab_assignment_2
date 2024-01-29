class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary


Empa = Employee(emp_id="161E90", name="Ramu", age=35, salary=59000)
Empb = Employee(emp_id="171E22", name="Tejas", age=30, salary=82100)
Empc = Employee(emp_id="171G55", name="Abhi", age=25, salary=100000)
Empd = Employee(emp_id="151K46", name="Jaya", age=32, salary=85000)

Emps = [Empa, Empb, Empc, Empd]


print("1.Age")
print("2.Name")
print("3.Salary")
F=int(input(""))
if F == 1:
    sort = sorted(Emps, key=lambda emp: emp.age)
elif F == 2:
    sort = sorted(Emps, key=lambda emp: emp.name)
elif F == 3:
    sort = sorted(Emps, key=lambda emp: emp.salary)

for i in sort:
    print("employee id:", i.emp_id)
    print(" name:", i.name)
    print(" age:", i.age)
    print("salary (pm):", i.salary)