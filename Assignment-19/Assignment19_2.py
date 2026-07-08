# Return multiplication of two numbers using lambda

def main():
    No1 = int(input("Enter a first number: "))
    No2 = int(input("Enter a second number: "))

    Mult = lambda Num1 , Num2 : Num1 * Num2

    print(f"The Multiplication of {No1} X {No2} is : {Mult(No1,No2)}")

if __name__ == "__main__":
    main()