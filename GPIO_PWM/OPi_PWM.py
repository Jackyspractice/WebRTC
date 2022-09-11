import OPi.GPIO as GPIO


##SG90
#Orange ---> Signal
#Red ---> Power (4.8-5V)
#Brown ---> Ground

# T = 50Hz / 20ms
#Degree
#0  ---> 0.5ms (High) 2.5%
#45 ---> 1ms 5%
#90 ---> 1.5ms 7.5%
#135 ---> 2ms 10%
#180 ---> 2.5ms 12.5%
frequency_Hz = 50
Duty_Cycle_Percent = 2.5
SG90_Degree = []
PWM_Class1 = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
PWM_Class2 = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)

class SG90:

    def __init__(self, degree, duty, cycle) -> None:

        self.degree = degree
        self.duty = duty
        self.cycle = 0.05

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

    def IO_init():
        print("Initlizating GPIO...\n")
        GPIO.setwarnings(False)
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setmode(GPIO.BCM) 對表BCM的PIN號
        #GPIO.setmode(GPIO.wiringPi) 適用於C++
        #HOW TO FIND PIN TABLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #cmd "gpio readall" (Need install wiring)
        #OR GOto
        # https://github.com/rm-hull/OPi.GPIO

    def Setting_PWM_Argument(self, degree): #Degree is defined by SG90 Argument

        if degree == 0:

        elif degree == 45:

        elif degree == 90:




if __name__ == "__main__":
