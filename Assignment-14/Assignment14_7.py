# Retuern True if number is divisible by 5

def main():
    print("Enter a number : ")
    num = int(input())
    Divide_five = lambda no1: True if no1 % 5 == 0 else False
    Ret = Divide_five(num)
    print(Ret)

if __name__ == "__main__":
    main()