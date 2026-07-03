#  checking numner is divisiable by 5 and 3 

def Chk_divide(num):
    if num % 3 == 0 and num % 5 == 0:
        return True

def main():
    print("Enter a number : ")
    num = int(input())

    Ret = Chk_divide(num)

    if Ret == True:
        print("Number",num,"is divisible by 3 and 5")
    else:
        print("Number",num,"is not divisible by 3 and 5")

if __name__ == "__main__":
    main()