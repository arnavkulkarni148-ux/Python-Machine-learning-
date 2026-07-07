# Addition of all elements in the list

def Addition_list(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

def main():
    print("Enter How many value you want in the list: ")
    value = int(input())
    num = []

    print("Enter a number: ")
    for i in range(value):
        value1 = int(input())
        num.append(value1)
    
    Ret = Addition_list(num)

    print("Addition of all numbers in the list is :",Ret)

if __name__ == "__main__":
    main()