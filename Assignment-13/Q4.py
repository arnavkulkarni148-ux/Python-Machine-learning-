# number converting into binary 
def Convert_binary(num):
    temp_num = num
    n1 = []
    while(temp_num > 0):
        remainder = temp_num % 2
        temp_num = temp_num // 2
        n1.append(remainder) 
    for digit in reversed(n1):   
        print(digit,end=" ")

def main():
    print("Enter a number : ")
    num = int(input())
    print("Binary number of",num,"is : ")
    Convert_binary(num)
if __name__ == "__main__":
    main()