# return minimum number in the list with reduce() and lambda ()
from functools import reduce 
def main():
    no = int(input("Enter how many numbers do you want in the list :"))
    num = []

    print("Enter a numbers: ")

    for i in range(no):
        value = int(input())
        num.append(value)
    min_number = lambda no1,no2: no1 if no1 < no2 else no2

    Data  = reduce(min_number,num)
    print("The minimum number in the list is:")
    print(Data)


if __name__ == "__main__":
    main()