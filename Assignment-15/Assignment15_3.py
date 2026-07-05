# list of odd numbers with filter() and lambda ()
def main():
    no = int(input("Enter how many numbers do you want in list: "))
    num = []

    print("Enter a numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)
    odd_number = lambda x : x % 2 !=0 

    Data = list(filter(odd_number,num))
    print("Odd numbers from the list are: ")
    print(Data)

if __name__ == "__main__":
    main()