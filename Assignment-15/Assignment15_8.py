# Returning numbers which is divisible by 3 and 5 with help of filter () and lambda()

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value = int(input())
        num.append(value)
    
    check_Divide = lambda no1 : (no1 % 3 == 0 and no1 % 5 == 0)

    Data = list(filter(check_Divide,num))

    print("The numbers which is divisible by 3 nad 5 are: ")
    print(Data)

if __name__ == "__main__":
    main()