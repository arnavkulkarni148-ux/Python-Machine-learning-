# Using lambda function returning power of two

def main():
    No = int(input("Enter a number which is you want to be the power of two : "))

    Power = lambda Num1 : 2 ** Num1

    print(f"The power of 2 with respect to {No} is {Power(No)}")

if __name__ == "__main__":
    main()