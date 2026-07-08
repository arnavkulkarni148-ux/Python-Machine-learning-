# using Filter map reduce

from functools import reduce

def main():
    no = int(input("Enter how many numbers do you want in the list : "))
    num = []
    # num1 = [4,34,36,76,68,24,89,23,86,90,45,70]

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Data1 = lambda No : No >= 70 and No <= 90

    Filter_number = list(filter(Data1,num))

    print("The List after filtering the Data is : ")
    print(Filter_number)

    Data2 = lambda No1 : No1 + 10

    Map_number = list(map(Data2,Filter_number))
    print("The list after maping the data is :")
    print(Map_number)

    Data3 = lambda No1 , No2 : No1 * No2

    Reduce_number = (reduce(Data3,Map_number))
    print("The list after reducing is : ")
    print(Reduce_number)



if __name__ == "__main__":
    main()