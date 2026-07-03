# Caluclator 

def addition(num1,num2):
    ans = num1 + num2
    return ans

def subtraction(num1,num2):
    ans = num1 - num2
    return ans

def multiplication(num1,num2):
    ans = num1 * num2
    return ans

def division(num1,num2):
    ans = num1 / num2
    return ans

def main():
    n1 = int(input("Enter a first number: "))
    n2 = int(input("Enter a second number: "))

    Ret1 = addition(n1,n2)
    print("The addition of",n1,"+",n2,"=",Ret1)

    Ret2 = subtraction(n1,n2)
    print("The subtraction of",n1,"-",n2,"=",Ret2)

    Ret3 = multiplication(n1,n2)
    print("The multiplication of",n1,"X",n2,"=",Ret3)

    Ret4 = division(n1,n2)
    print("The division of",n1,"/",n2,"=",Ret4)


if __name__ == "__main__":
    main()