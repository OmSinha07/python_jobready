class C2dVec:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def __str__(self):
        return(f"{self.i}i + {self.j}")
class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j )
        self.k=k
        self.j = j
    def __str__(self):
        return(f"{self.i}i + {self.j} + {self.k}k") 
v2d =C2dVec(1,3)
v3d =C3dVec(1,9,7)
print(v2d)
print(v3d)