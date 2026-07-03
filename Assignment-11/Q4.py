# reverse the number1
def main():
    print("Enter a number: ")
    num = int(input())
    num1 = num
    num2 = 0
    reverse_number = 0

    while(num1 > 0):
        num2 = num1 % 10
        reverse_number = (reverse_number * 10) + num2 
        num1 = num1 // 10
    print("Reverse nummber of",num,"is :",reverse_number)

if __name__ == "__main__":
    main()
