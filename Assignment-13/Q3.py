# Perfect number checker
def Check_PerfectNumber(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False

def main():
    print("Enter a number :")
    num = int(input())
    Ret = Check_PerfectNumber(num)

    if Ret == True:
        print(num,"is a pefect number")
    else:
        print(num,"is not a perfect number")




if __name__ == "__main__":
    main()