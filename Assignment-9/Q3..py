# Square of number 

def Square_number(num):
    square = num * num
    return square

def main():
    print("Enter a number : ")
    num = int(input())

    Ret = Square_number(num)
    print("Square of",num, "is :",Ret)

if __name__ == "__main__":
    main()
