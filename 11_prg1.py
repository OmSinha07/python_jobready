class programmer:
    company ="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getinfo(self):
        print(f"name of employee is {self.name}")
        print(f"porduct name is {self.product}")        

harry=programmer("harry","nykaa")
harry.getinfo()
