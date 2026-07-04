# Return multiplication using lambda function

def main():
    print("Enter a first number: ")
    num1 = int(input())
    print("Enter a second number: ")
    num2 = int(input())

    Mult_number = lambda no1,no2: no1 * no2 
    Ret = Mult_number(num1,num2)

    print("Multiplication is: ")
    print(num1,"X",num2,"=",Ret)

if __name__ == "__main__":
    main()