class programmmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
    def method(self):
        print(f"In {self.company}. {self.name} is a employee whose salary is {self.salary}$ per month and his pin code is {self.pin}.")

p = programmmer("Hassaan", 25000, 313885)
# print(p.company, p.name, p.salary, p.pin)
p2 = programmmer("Amir", 10000, 447891)
p.method()
p2.method()