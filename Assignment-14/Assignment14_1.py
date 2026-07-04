# Square of number using lambda

def main():
    print("Enter a number: ")
    num = int(input())

    Square = lambda no: no * no  # Lambda function 

    print("Square of",num,"is:",Square(num))

if __name__ == "__main__":
    main()
    