class CalcImplementation():
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        
        return a / b


class BuggyCalcImplementation():
    def add(self, a, b):
        return abs(a + b)

    def subtract(self, a, b):
        return abs(a - b)

    def multiply(self, a, b):
        a = abs(a)
        b = abs(b)
        return a * b

    def divide(self, a, b):
        return a / b
    

class Calculator():
    def __init__(self, implementation):
        self.implementation = implementation
    
    def add(self, a, b):
        return self.implementation.add(a,b)

    def subtract(self, a, b):
        return self.implementation.subtract(a,b)

    def multiply(self, a, b):
        return self.implementation.multiply(a,b)

    def divide(self, a, b):
        return self.implementation.divide(a,b)

