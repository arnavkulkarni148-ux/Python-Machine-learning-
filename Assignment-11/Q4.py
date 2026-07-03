# reverse the number1

def Reverse_number(num):
    num1 = num
    num2 = 0
    reverse_number = 0

    while(num1 > 0):
        num2 = num1 % 10
        reverse_number = (reverse_number * 10) + num2 
        num1 = num1 // 10
    return reverse_number

def main():
    print("Enter a number: ")
    num = int(input())
    Ret = Reverse_number(num)

    print("Reverse nummber of",num,"is:",Ret)

if __name__ == "__main__":
    main()
