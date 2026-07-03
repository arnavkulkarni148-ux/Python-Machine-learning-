# count the digit in the number 
def main():
    count = 0
    
    print("Enter a number: ")
    num = int(input())
    num1 = num 

    while(num1 > 0):
        num1 = num1 // 10
        count = count + 1
    print("The digit in the number",num,"is",count)

if __name__ == "__main__":
    main()