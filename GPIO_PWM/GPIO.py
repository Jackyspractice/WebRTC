import OPi.GPIO as GPIO
import time

class GPIO_Control:


    def IO_init(self):

        print("Initlizating GPIO...\n")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setmode(GPIO.BCM) 對表BCM的PIN號
        #GPIO.setmode(GPIO.wiringPi) 適用於C++
        #HOW TO FIND PIN TABLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #cmd "gpio readall"
        #OR GOto
        # https://github.com/rm-hull/OPi.GPIO

    def Setting_Pin(self):

        IO_setting = []
        IO_setting.clear()

        PinNumber = 777
        while PinNumber > 26 or PinNumber < 0:
            PinNumber = int(input("Please input PinNumber to start[0-26]...."))
            if PinNumber > 26 or PinNumber < 0:
                print("Unavailable PinNumber, Please renter...\n")

        IO_setting.append(PinNumber)
        
        Pin_value = 777
        while Pin_value not in [0, 1]:
            Pin_value = int(input("Please input value of pin to start[0, 1]...."))

        IO_setting.append(Pin_value)

        return IO_setting


    
    def Output(self, pinsetting):

        print("Outputting Your setting....\n")
        GPIO.setup(pinsetting[0], GPIO.OUT)
        GPIO.output(pinsetting[0], pinsetting[1])
        print("Output Finish...\n")

def Sleep(sec):

    print("Sleep for " + str(sec) + " sec")
    for i in range (0, sec):
        print("Remain " + str(sec - i - 1) + " sec", end = "\r")
        time.sleep(1)


def main():

    GPIO = GPIO_Control()

    GPIO.IO_init()
    Setting = GPIO.Setting_Pin()
    GPIO.Output(Setting)
    Sleep(5)


if __name__ == "__main__":

    GPIO.cleanup()
    main()
