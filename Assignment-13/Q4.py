# number converting into binary  

def main():
    print("Enter a number : ")
    num = int(input())
    temp_num = num
    n1 = []
    while(temp_num > 0):
        remainder = temp_num % 2
        temp_num = temp_num // 2
        n1.append(remainder)
    print("Binary number of",num,"is : ")
    for digit in reversed(n1):   
        print(digit,end=" ")
if __name__ == "__main__":
    main()