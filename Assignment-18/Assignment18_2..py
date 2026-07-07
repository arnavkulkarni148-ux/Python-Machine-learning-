# Return maximum number from list

def Maximum_number(lst):
    
    max_number = max(lst)
    return max_number

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter numbers: ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Ret = Maximum_number(num)

    print("Maximum Number in the list is:",Ret)

if __name__ == "__main__":
    main()
