import schedule
import time
import datetime

def WriteFile():
    fobj = open("Marvellous.txt","a")

    CurrentTime = datetime.datetime.now()

    fobj.write(f"Task executed at:{CurrentTime}\n")

    fobj.close()

def main():
    print("Schedule Started")

    schedule.every(5).minutes.do(WriteFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()