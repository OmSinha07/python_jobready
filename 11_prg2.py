class calculator:
    def __init__(self,n):
        self.no=n
    def square(self):
        cal=self.no*self.no
        print(cal)
    def sqrt(self):
        sq=self.no**0.5
        print(sq)
    def cube(self):
        cube=self.no**3
        print(cube)
om=calculator(5)
om.square()
om.sqrt()
om.cube()

