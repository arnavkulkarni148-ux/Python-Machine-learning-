# Area of circle
def Area_circle(radius1):
    Area = 3.145 * radius1 * radius1
    return Area 
    
def main():
    print("Enter a radius of a circle: ")
    radius = int(input())
    Ret = Area_circle(radius)

    print("Area of circle is:",Ret)

if __name__ == "__main__":
    main()