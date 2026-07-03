# even number till the input number

def Even_no(num):
     for i in range(1,num+1):
        if i % 2 == 0:
            print(i)

def main():
    print("Enter a number : ")
    num = int(input())
    print("Even number till",num,"is :")
    
    Even_no(num)

if __name__ == "__main__":
    main()