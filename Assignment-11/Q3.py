# sum of the digits of the number 
def main():
    print("Enter a number: ")
    num = int(input())
    sum = 0
    num1 = num

    while(num1 > 0):
        num2 = 0
        num2 = num1 % 10
        sum = sum + num2
        num1 = num1 // 10

    print("The sum of the number in",num,"is",sum)
if __name__ == "__main__":
    main()
