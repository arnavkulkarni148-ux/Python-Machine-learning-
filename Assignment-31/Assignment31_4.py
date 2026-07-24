import schedule
import time
import datetime

def CreateFile():
    CurrentTime = datetime.datetime.now()
    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName,"w")

    fobj.write("Log File created Succesufully...\n")
    fobj.write("Cration Time: ")
    fobj.write( CurrentTime.strftime("%d_%m_%Y_%H_%M_%S"))
    print("File created Succesfully")

    fobj.close()

def main():

    schedule.every(10).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()