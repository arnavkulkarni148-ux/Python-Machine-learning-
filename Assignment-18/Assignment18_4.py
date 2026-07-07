# Return frequency of number in the list

def Frequency_number(lst,Number_Search):
    # No = int(input("Enter a number to search: "))
    count = 0
    for i in lst:
        if Number_Search == i:
            count = count + 1
    return count 
        

def main():
    no = int(input("Enter how many numbers do you want in the list: "))
    num = []

    print("Enter a numbers : ")
    for i in range(no):
        value = int(input())
        num.append(value)

    Search_number = int(input("Enter a number to search: "))
    
    Ret = Frequency_number(num,Search_number)

    print(f"The frequency of number {Search_number} is:{Ret}")

if __name__ == "__main__":
    main()
