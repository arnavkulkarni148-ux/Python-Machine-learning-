# sum of the digits of the number 
def sum_number(num):
    sum = 0
    num1 = num

    while(num1 > 0):
        num2 = 0
        num2 = num1 % 10
        sum = sum + num2
        num1 = num1 // 10
    return sum

def main():
    print("Enter a number: ")
    num = int(input())

    Ret = sum_number(num)

    print("The sum of the number in",num,"is",Ret)
if __name__ == "__main__":
    main()
