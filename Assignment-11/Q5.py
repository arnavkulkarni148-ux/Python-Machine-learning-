# check palindrome
def main():
    print("Enter a number: ")
    num = int(input())
    num1 = num
    num2 = 0
    reverese_number = 0

    while(num1 > 0):
        num2 = num1 % 10
        reverese_number = (reverese_number * 10) + num2
        num1 = num1 // 10
    if num == reverese_number:
        print(num,"Is palindrome")
    else:
        print(num,"Is not palindrome")

if __name__ == "__main__":
    main()