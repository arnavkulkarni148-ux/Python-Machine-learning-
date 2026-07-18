class Arithmetic():
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    def Accept(self):
        self.Value1 = int(input("Enter a Value 1 : "))
        self.Value2 = int(input("Enter a value 2 : "))
        
    
    def Addition(self):
        add = self.Value1 + self.Value2
        return add
    
    def Subtraction(self):
        sub = self.Value1 - self.Value2
        return sub
    
    def Multiplication(self):
        mult = self.Value1 * self.Value2
        return mult
    
    def Division(self):
        if self.Value2 == 0:
            print("Division Not possible")
            return "Not Possible by zero"
        
        div = self.Value1 / self.Value2
        return div
    
def main():

    Obj1 = Arithmetic()
    Obj2 = Arithmetic()

    Obj1.Accept()
    Ret1 = Obj1.Addition()
    Ret2 = Obj1.Subtraction()
    Ret3 = Obj1.Multiplication()
    Ret4 = Obj1.Division()
    print(f"\nThe addtion is:{Ret1}")
    print(f"The Subtraction is :{Ret2}")
    print(f"The Multiplication is : {Ret3}")
    print(f"The Division is : {Ret4}")

    Obj2.Accept()
    Ret_1 = Obj2.Addition()
    Ret_2 = Obj2.Subtraction()
    Ret_3 = Obj2.Multiplication()
    Ret_4 = Obj2.Division()
    print(f"\nThe addtion is:{Ret_1}")
    print(f"The Subtraction is :{Ret_2}")
    print(f"The Multiplication is : {Ret_3}")
    print(f"The Division is : {Ret_4}")

if __name__ == "__main__":
    main()