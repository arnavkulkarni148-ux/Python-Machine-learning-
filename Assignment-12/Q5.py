def main():
    print("Enter a number: ")
    num = int(input())

    for i in range(num,0,-1):
        print(i,end=" ")

if __name__ == "__main__":
    main()