class ComplexNumber:
    
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __add__(self,other):
        return ComplexNumber(self.real+other.real,self.img+other.imag)
    
    
    c1=complex(1,2)
    c2=complex(3,4)
    c3 = c1 + c2
    print(c3.real,"+ i",c3.imag)