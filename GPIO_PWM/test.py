import time

def Sleep(sec):

    print("Sleep for " + str(sec) + " sec")
    for i in range (0, sec):
        print("Remain " + str(sec - i - 1) + " sec", end = "\r")
        time.sleep(1)

Sleep(5)