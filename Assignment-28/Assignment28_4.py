import os

def main():
    print("Enter a file name from you want to copy : ")
    ExistingFile = input()
    print("Enter a file name where you want to copy : ")
    CopyFile = input()

    Ret = os.path.exists(ExistingFile)

    if Ret == True:
        fobj = open(ExistingFile,"r")
        fobj1 = open(CopyFile,"w")

        for line in fobj:
            fobj1.write(line)
        print("Lines are copy succesfully...")
        fobj.close()
        fobj1.close()

    else:
        print("File is not present") 

if __name__ == "__main__":
    main()