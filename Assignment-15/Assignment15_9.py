# Return product of list using reduce() and lambda()

from functools import reduce

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value = int(input())
        num.append(value)
    
    product_number = lambda no1,no2: no1*no2

    Data = reduce(product_number,num)
    print(f"The product of all numbers in the list is : {Data}")

if __name__ == "__main__":
    main()
