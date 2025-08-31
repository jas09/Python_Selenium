class Calculator:
    num = 100 #calss variable

    #default Constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

d = Calculator(2,3)
print(d.getData())
print(d.summation())

e = Calculator(4,5)
print(e.getData())
print(e.summation())