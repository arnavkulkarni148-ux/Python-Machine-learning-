# Factorial of number

def Factorial_No(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

def main():
    print("Enter a number for factorial : ")
    num = int (input())
    Ret = Factorial_No(num)

    print("Factorial of",num,"is:",Ret)

if __name__ == "__main__":
    main()