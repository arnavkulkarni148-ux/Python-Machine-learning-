# count the digit in the number 

def count_number(num):
    count = 0
    while(num > 0):
        count = count + 1
        num = num // 10
    return count
    
def main():
    # count = 0
    
    print("Enter a number: ")
    num = int(input())
    Ret = count_number(num)

    # while(num1 > 0):
    #     num1 = num1 // 10
    #     count = count + 1
    print("The digit in the number is:",Ret)

if __name__ == "__main__":
    main()