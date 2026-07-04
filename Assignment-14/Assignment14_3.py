# Return th maximum number
def main():
    print("Enter a first number")
    num1 = int(input())
    print("Enter a second number")
    num2 = int(input())

    max_number = lambda no1 , no2 : no1 if no1 > no2 else no2 

    Ret = max_number(num1,num2)
    print("Maximum number from",num1,"and",num2,"is",Ret)

if __name__ == "__main__":
    main()
