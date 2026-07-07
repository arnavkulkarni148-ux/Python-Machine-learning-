# Returninig the digit in the number 
def Count_number(No):
    count = 0
    while(No > 0):
        count = count + 1
        No = No // 10
    return count

def main():
    Num = int(input("Enter a number : "))
    Ret = Count_number(Num)

    print(f"The length of number {Num} is {Ret}")


if __name__ == "__main__":
    main()