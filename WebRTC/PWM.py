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

    def Open(self, which_box): #clockwise, turns

        global PWM, Box_GPIO_port

        gpio.setcfg(port.Box_GPIO_port[which_box - 1], 1)
        
        print("Opening...")

        PWM.start(SG90_Degree[0].duty)
        sleep(runtime)

        PWM.changeDutyCycle(SG90_Degree[1].duty)

    def Close(self, which_box):    #counter clockwise turns

        global PWM, Box_GPIO_port

        print("Closing...")

        gpio.setcfg(port.Box_GPIO_port[which_box - 1], 0)

        PWM.changeDutyCycle(SG90_Degree[2].duty)
        sleep(runtime)

        PWM.stop()

    def initial_SG90(self): #initial Obj SG90

        SGobj = SG90()
        SGobj.Set_degree_argument()

    def GPIO_initial(self):

        global Box_GPIO_port
        
        for i in range (0, len(Box_GPIO_port)):

            gpio.setcfg(port.Box_GPIO_port[i], gpio.OUTPUT)
            gpio.setcfg(port.Box_GPIO_port[i], 0)

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
    pwm.active("2")