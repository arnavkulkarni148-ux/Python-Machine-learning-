# Odd number till that input number
def Odd_no(num):
    for i in range(1,num+1):
        if i % 2 != 0:
            print(i)
def main():
    print("Enter a number")
    num = int(input())

    print("Odd number till",num,"is:")
    Odd_no(num)
   

if __name__ == "__main__":
    main()
