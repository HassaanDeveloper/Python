class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"The Cube of {self.n} is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The SquareRoot of {self.n} is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hey there!")

n = int(input("Enter the number: "))
a = calculator(n)
a.hello()
a.square()
a.cube()
a.squareroot()