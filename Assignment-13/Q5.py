# Display grade using marks 
def Marks_grade(marks):
    if marks >= 75 and marks <= 100:
        return "Distinction"
    elif marks >= 60 and marks < 75:
        return "First Class"
    elif marks >=50 and marks < 60:
        return "Second Class"
    elif marks < 50 and marks >= 0:
        return "Fail"
    else:
        return "Invalid Marks"
    
def main():
    print("Enter a marks of student : ")
    marks = int(input())
    Ret = Marks_grade(marks)
    print("Grade is:",Ret)

if __name__ == "__main__":
    main()