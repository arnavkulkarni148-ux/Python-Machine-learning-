# Factor of a number

def Factor_number(num):
    for i in range(1,num):
        if num % i == 0:
            print(i,end=" ")

def main():
    print("Enter a number: ")
    num = int(input())
    print("Factor of",num,"is:")

    Factor_number(num)
    
if __name__ == "__main__":
    main()