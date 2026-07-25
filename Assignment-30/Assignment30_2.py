
import schedule
import time
import datetime

def Display():
    print("Current Date and Time:",datetime.datetime.now())
def main():
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()