class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The value of vector is: {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(4,7)
b = ThreeDvector(4, 7, 9)
b.show()