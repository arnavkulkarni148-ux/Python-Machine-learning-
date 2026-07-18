class Numbers():
    def __init__(self,A):
        self.Value = A

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        if self.Value == 2:
            return True
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        total = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                total = total + i

        if total == self.Value:
            return True
        else:
            return False
    
    def Factors(self):
        print("Factors are:", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total = total + i
        return total
    
def main():

    Obj1 = Numbers(11)
    Obj2 = Numbers(10)

    Ret1 = Obj1.ChkPrime()
    print(Ret1)
    Ret2 = Obj1.ChkPerfect()
    print(Ret2)
    Obj1.Factors()
    Ret3 = Obj1.SumFactors()
    print(Ret3)

    print()

    Ret4 = Obj2.ChkPrime()
    print(Ret4)
    Ret5 = Obj2.ChkPerfect()
    print(Ret5)
    Obj2.Factors()
    Ret6 = Obj2.SumFactors()
    print(Ret6)

if __name__ == "__main__":
    main()