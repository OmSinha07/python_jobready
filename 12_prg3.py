class Employee:
    salary = 1000
    inc=1.5
    @property
    def SalaryAfterInc(self):
        return self.salary*self.inc
   
    @SalaryAfterInc.setter
    def SalaryAfterInc(self,sai):
        self.inc=sai/self.salary

e =Employee()
print(e.SalaryAfterInc)
print(e.inc)
e.SalaryAfterInc=2000
print(e.inc)