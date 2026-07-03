# sum of n natural numbers
def Sum_No(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    return sum

def main():
    print("Enter a number : ")
    num = int(input())
    Ret = Sum_No(num)

    print("Sum upto",num,"is:",Ret)

if __name__ == "__main__":
    main()