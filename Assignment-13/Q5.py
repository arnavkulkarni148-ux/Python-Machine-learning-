# Display grade using marks 

def main():
    print("Enter a marks of student : ")
    marks = int(input())

    if marks >= 75 and marks <= 100:
        print("Grade of a student is: Distiction!")
    elif marks >= 60 and marks < 75:
        print("Grade of a student is: First Class!")
    elif marks >=50 and marks < 60:
        print("Grade of a student is: Second Class!")
    elif marks < 50 and marks >= 0:
        print("Grade of a student is: Fail!")
    else:
        print("Invalid Marks..")
    

if __name__ == "__main__":
    main()