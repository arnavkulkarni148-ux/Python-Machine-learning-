class BankAccount():
    ROI = 10.5
    def __init__(self,A,B):
        self.Name = A
        self.Amount = B
    
    def Display(self):
        print(f"Account holder name is : {self.Name}")
        print(f"Current acount balance is: {self.Amount}")

    def Deposit(self):
        amount = int(input("Enter a amount you want to deposit: "))
        self.Amount = self.Amount + amount
        print(f"Your current balance is : {self.Amount}")

    def Withdraw(self):
        amount = int(input("Enter how many amount do yo want to withdraw: "))
        if amount <= self.Amount:
            self.Amount = self.Amount - amount
            print(f"After withdrawel of amount your current balance is : {self.Amount}")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
def main():

    Obj1 = BankAccount("Arnav" , 50000)
    Obj2 = BankAccount("Atharva" , 45000 )

    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    Ret1 = Obj1.CalculateInterest()
    print(f"Interest is : {Ret1}")

    print()

    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Ret2 = Obj2.CalculateInterest()
    print(f"Interest is: {Ret2}")

if __name__ == "__main__":
    main()