from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

SG90_Degree = []
PWM = None
runtime = 5
Box_GPIO_port = ["PA1", "PA0", "PA3", "PA7", "PA19", "PA18"] #11, 13, 15, 12, 16, 18

class SG90:

    def __init__(self, degree = None, duty = None, frequence = None) -> None:

        self.degree = degree
        self.duty = duty
        self.frequence = 50 #50Hz

    def Set_degree_argument(self):
        
        SG90_Degree.clear()

        Degree_0 = SG90()
        Degree_0.degree = 0
        Degree_0.duty = 2
        SG90_Degree.append(Degree_0)

        Degree_90 = SG90()
        Degree_90.degree = 90
        Degree_90.duty = 7
        SG90_Degree.append(Degree_90)

        Degree_180 = SG90()
        Degree_180.degree = 180
        Degree_180.duty = 10
        SG90_Degree.append(Degree_180)

class PWM_Control:

    def GPIO_set_HIGH(self, which_box):

        global Box_GPIO_port

        if Box_GPIO_port[which_box - 1] == "PA1":
            gpio.setcfg(port.PA1, 1)

        elif Box_GPIO_port[which_box - 1] == "PA0":
            gpio.setcfg(port.PA0, 1)

        elif Box_GPIO_port[which_box - 1] == "PA3":
            gpio.setcfg(port.PA3, 1)
        
        elif Box_GPIO_port[which_box - 1] == "PA7":
            gpio.setcfg(port.PA7, 1)
        
        elif Box_GPIO_port[which_box - 1] == "PA19":
            gpio.setcfg(port.PA19, 1)
        
        elif Box_GPIO_port[which_box - 1] == "PA18":
            gpio.setcfg(port.PA18, 1)

    def GPIO_set_LOW(self, which_box):

        global Box_GPIO_port

        if Box_GPIO_port[which_box - 1] == "PA1":
            gpio.setcfg(port.PA1, 0)

        elif Box_GPIO_port[which_box - 1] == "PA0":
            gpio.setcfg(port.PA0, 0)

        elif Box_GPIO_port[which_box - 1] == "PA3":
            gpio.setcfg(port.PA3, 0)
        
        elif Box_GPIO_port[which_box - 1] == "PA7":
            gpio.setcfg(port.PA7, 0)
        
        elif Box_GPIO_port[which_box - 1] == "PA19":
            gpio.setcfg(port.PA19, 0)
        
        elif Box_GPIO_port[which_box - 1] == "PA18":
            gpio.setcfg(port.PA18, 0)

    def Open(self, which_box): #clockwise, turns

        global PWM

        self.GPIO_set_HIGH(which_box)

        print("Opening...")

        PWM.start(SG90_Degree[0].duty)
        sleep(runtime)

        PWM.changeDutyCycle(SG90_Degree[1].duty)

    def Close(self, which_box):    #counter clockwise turns

        global PWM

        print("Closing...")


        PWM.changeDutyCycle(SG90_Degree[2].duty)
        sleep(runtime)
        
        self.GPIO_set_LOW(which_box)

        PWM.stop()

    def initial_SG90(self): #initial Obj SG90

        SGobj = SG90()
        SGobj.Set_degree_argument()

    def GPIO_initial(self):
        
        gpio.setcfg(port.PA1, gpio.OUTPUT)
        gpio.setcfg(port.PA1, 0)
        gpio.setcfg(port.PA0, gpio.OUTPUT)
        gpio.setcfg(port.PA0, 0)
        gpio.setcfg(port.PA3, gpio.OUTPUT)
        gpio.setcfg(port.PA3, 0)
        gpio.setcfg(port.PA7, gpio.OUTPUT)
        gpio.setcfg(port.PA7, 0)
        gpio.setcfg(port.PA19, gpio.OUTPUT)
        gpio.setcfg(port.PA19, 0)
        gpio.setcfg(port.PA18, gpio.OUTPUT)
        gpio.setcfg(port.PA18, 0)

    def initial(self):  #initial SG90 Argument & PWM frequence/Port

        global PWM

        gpio.init()
        self.GPIO_initial()
        self.initial_SG90()
        PWM = OrangePwm(SG90_Degree[0].frequence, port.PA6)

    def active(self, which_box):

        try:
            self.Open(int(which_box))
            print("Waiting for Close...")
            sleep(runtime * 2)
            self.Close(int(which_box))

            return True
        except:

            return False

if __name__ == "__main__":

    pwm = PWM_Control()
    pwm.initial()
    
    while 1:
        
        pwm.GPIO_initial()
        num = input("input num: ")
        pwm.active(num)