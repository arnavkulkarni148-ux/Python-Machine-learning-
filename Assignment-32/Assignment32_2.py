import os
import schedule
import time
import datetime

def MonitorFile(FileName):

    if os.path.exists(FileName):
        size = os.path.getsize(FileName)
        CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y:%H-%M-%S")

        fobj = open("FIleSizeLog.txt","a")

        fobj.write(f"File Path :{FileName}\n")
        fobj.write(f"File size in bytes :{size}\n")
        fobj.write(f"Date and time :{CurrentTime}")

        fobj.close()
        print("File Log updated...")
    else:
        print("File does not exists..")

def main():
    print("Enter a file name: ")
    FileName = input()

    schedule.every(30).seconds.do(MonitorFile,FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()