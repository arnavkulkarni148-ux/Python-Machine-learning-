#  Returning the count of even numbers using filter() and lambda()

def main():
    no = int(input("Enter how many numbers do you want in the list : "))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value = int(input())
        num.append(value)
    
    Even_numbers = lambda no1 : no1 % 2 == 0

    Data = list(filter(Even_numbers,num))

    Count = len(Data)

    print("The Even numbers in the list are : ")
    print(Data)
    print(f"The count of Even numbers in the list is : {Count}")
if __name__ == "__main__":
    main()