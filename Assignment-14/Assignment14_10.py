# Maximum of three numbers
def main():
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    num3 = int(input("Enter a third number: "))

    Max_ThreeNumber = lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else (no2 if no2 > no3 else no3)

    Ret = Max_ThreeNumber(num1,num2,num3)
    print("The maximum number between",num1,num2,"and",num3,"is :")
    print(Ret)

if __name__ == "__main__":
    main()