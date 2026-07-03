# cube of number

def Cube_number(num):
    cube = num * num * num
    return cube

def main():

    print("Enter a number : ")
    num = int(input())

    Ret = Cube_number(num)
    print("Cube of", num, "is :",Ret)
    
if __name__ == "__main__":
    main()
