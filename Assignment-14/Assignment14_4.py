# Return th minimum number
def main():
    print("Enter a first number")
    num1 = int(input())
    print("Enter a second number")
    num2 = int(input())

    min_number = lambda no1 , no2 : no1 if no1 < no2 else no2 

    Ret = min_number(num1,num2)
    print("Minimum number from",num1,"and",num2,"is",Ret)

if __name__ == "__main__":
    main()
