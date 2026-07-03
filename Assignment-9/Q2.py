# check greater number

def ChkGreater(no1,no2):
    if no1 > no2 :
        print(no1, "is greater")
    else:
        print(no2, "is greater")

def main():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    ChkGreater(num1,num2)

if __name__ == "__main__":
    main()