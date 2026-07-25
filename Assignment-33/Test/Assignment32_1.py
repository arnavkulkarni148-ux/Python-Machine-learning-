import schedule
import time
import datetime

def CreateFile():
    CurrentTime = datetime.datetime.now()

    Filename = "file_"+CurrentTime.strftime("%d_%m_%Y_%H_%M_%S")+".txt"

    fobj = open(Filename,"a")

    fobj.write(f"Filename :{Filename}\n")
    fobj.write(f"Creation Date : {CurrentTime.strftime("%d-%m-%Y")}\n")
    fobj.write(f"Creation Time :{CurrentTime.strftime("%H-%M-%S")}")

    fobj.close()

def main():
    print("Scheduling Started...")
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()