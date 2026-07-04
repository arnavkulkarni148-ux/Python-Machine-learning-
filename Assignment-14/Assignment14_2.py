# Cube of number using lambda

def main():
    print("Enter a number: ")
    num = int(input())

    Cube = lambda no: no * no * no     # Lambda function 

    print("Cube of",num,"is:",Cube(num))

if __name__ == "__main__":
    main()
    