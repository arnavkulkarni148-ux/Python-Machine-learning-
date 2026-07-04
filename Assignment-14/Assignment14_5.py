#  Return true if number is even and false if not

def main():
    print("Enter a number : ")
    num = int(input())

    Even_number = lambda no1 : True if no1 %2 == 0 else False
    Ret = Even_number(num)
    print(Ret)

if __name__ == "__main__":
    main()