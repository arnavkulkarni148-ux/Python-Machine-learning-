# Area of rectangle
def Area_rectangle(length1,breadth2):
     Area = length1 * breadth2
     return Area

def main():
    print("Enter a length of rectangle : ")
    length = int(input())
    print("Enter a breadth of rectangle : ")
    breadth = int(input())

    Ret = Area_rectangle(length,breadth)

    print("Area of rectangle is :",Ret)
if __name__ == "__main__":
    main()