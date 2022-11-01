from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

SG90_Degree = []
PWM = None
runtime = 5

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

    def Open(self): #clockwise, turns

        global PWM
        
        print("Opening...")

        PWM.start(SG90_Degree[0].duty)
        sleep(runtime)

        PWM.changeDutyCycle(SG90_Degree[1].duty)

    def Close(self):    #counter clockwise turns

        global PWM

        print("Closing...")

        PWM.changeDutyCycle(SG90_Degree[2].duty)
        sleep(runtime)

        PWM.stop()

    def initial_SG90(self): #initial Obj SG90

        SGobj = SG90()
        SGobj.Set_degree_argument()

    def initial(self):  #initial SG90 Argument & PWM frequence/Port

        global PWM

        gpio.init()
        self.initial_SG90()
        PWM = OrangePwm(SG90_Degree[0].frequence, port.PA6)

    def active(self):

        global PWM

        PWM.Open()
        print("Waiting for Close...")
        sleep(runtime)
        PWM.Close()

if __name__ == "__main__":

    pwm = PWM_Control()
    pwm.initial()
    pwm.active()