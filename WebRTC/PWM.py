from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

SG90_Degree = []
PWM = None
Turns = 5

class SG90:

    def __init__(self, degree = None, duty = None, frequence = None) -> None:

        self.degree = degree
        self.duty = duty
        self.frequence = 50 #50Hz

    def Set_degree_argument(self):
        
        SG90_Degree.clear()

        Degree_0 = SG90()
        Degree_0.degree = 0
        Degree_0.duty = 2.5
        SG90_Degree.append(Degree_0)

        Degree_45 = SG90()
        Degree_45.degree = 45
        Degree_45.duty = 5
        SG90_Degree.append(Degree_45)

        Degree_90 = SG90()
        Degree_90.degree = 90
        Degree_90.duty = 7.5
        SG90_Degree.append(Degree_90)

        Degree_135 = SG90()
        Degree_135.degree = 135
        Degree_135.duty = 10
        SG90_Degree.append(Degree_135)

        Degree_180 = SG90()
        Degree_180.degree = 180
        Degree_180.duty = 12.5
        SG90_Degree.append(Degree_180)

class PWM_Control:

    def Open(): #clockwise, turns

        print("Opening...")

        global PWM

        PWM.start(SG90_Degree[0].duty)
        sleep(0.5)

        for j in range (0, Turns):

            print("Turns:" , j)

            for i in range (1, 5):

                PWM.changeDutyCycle(SG90_Degree[i].duty)
                sleep(0.5)


        PWM.stop()

    def Close():    #counter clockwise turns

        print("Closing...")

        PWM.start(SG90_Degree[0].duty)
        sleep(0.5)

        for j in range (0, Turns):

            print("Turns:", j)

            for i in range (1, 5):

                PWM.changeDutyCycle(SG90_Degree[5 - i].duty)
                sleep(0.5)


        PWM.stop()

    def initial_SG90(self): #initial Obj SG90

        SGobj = SG90()
        SGobj.Set_degree_argument()

    def initial(self):  #initial SG90 Argument & PWM frequence/Port

        global PWM

        gpio.init()
        self.initial_SG90()
        PWM = OrangePwm(SG90_Degree[0].frequence, port.PA6)

    def Reset():    #reset sg90 to 0 degree

        global PWM

        PWM.start(SG90_Degree[0].duty)
        PWM.stop()

