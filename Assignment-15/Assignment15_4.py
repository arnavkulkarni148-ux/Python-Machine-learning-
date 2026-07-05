# addition of numbers with reduce() and lambda()
from functools import reduce

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value  = int(input())
        num.append(value)
    
    Addition_number = lambda no1,no2 : no1 + no2
    Data = reduce(Addition_number,num)

    print("The addtion of number in the list are: ")
    print(Data)
if __name__ == "__main__":
    main()