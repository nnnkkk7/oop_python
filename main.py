class Employee:
    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)    

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )


emp1 = Employee('nobu', 'yoshi', 2000)
emp2 = Employee('test', 'user', 70000)

print(emp1.fullname())
print(emp2.email)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

## インスタンスの中身
print(emp1.__dict__)

## empの数
print(Employee.num_of_emps)