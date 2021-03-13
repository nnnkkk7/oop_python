class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    ##フルネームをに整形   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)    


emp1 = Employee('nobu', 'yoshi', 2000)
emp2 = Employee('test', 'user', 70000)

print(emp1.fullname())
print(emp2.email)
