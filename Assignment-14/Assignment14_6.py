# Return True if number is odd otherwise return False 
def main():
    print("Enter a number : ")
    num = int(input())

    Odd_number = lambda no1: True if no1 % 2 !=0 else False

    Ret = Odd_number(num)
    print(Ret)


if __name__ == "__main__":
    main()
