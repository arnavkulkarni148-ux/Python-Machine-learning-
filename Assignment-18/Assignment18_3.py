# Return minimum number from list

def Minimum_number(lst):
    
    min_number = min(lst)
    return min_number

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Ret = Minimum_number(num)

    print("Minimum Number in the list is:",Ret)

if __name__ == "__main__":
    main()
