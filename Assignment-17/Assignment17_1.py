# Importing Module 

import Arithmetic

def main():
    No1 = int(input("Enter a first number : "))
    No2 = int(input("Enter a second number : "))

    Ret1 = Arithmetic.Add(No1,No2)
    print(f"\nThe addition of {No1} + {No2} = {Ret1}") 
    
    Ret2 = Arithmetic.Sub(No1,No2)
    print(f"The subtraction of {No1} - {No2} = {Ret2}")
    
    Ret3 = Arithmetic.Mult(No1,No2)
    print(f"The multiplication of {No1} X {No2} = {Ret3}")
    
    Ret4 = Arithmetic.Div(No1,No2)
    print(f"The division of {No1} / {No2} = {Ret4}")   


if __name__ == "__main__" :
    main()