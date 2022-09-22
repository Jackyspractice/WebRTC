from pyA20.gpio import gpio
from pyA20.gpio import port

#To-dos
#modify /usr/local/bin/python --- pyA20.gpio mapping.h (add new PA6)
#https://github.com/nvl1109/orangepi_zero_gpio/blob/master/pyA20/gpio/mapping.h
#https://github.com/duxingkei33/orangepi_PC_gpio_pyH3



from time import sleep
from orangepwm import *


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

gpio.init()

# Set GPIO pin PA6 as PWM output with a frequency of 50 Hz
pwm = OrangePwm(50, port.PA6)

# Start PWM output with a duty cycle of 20%. The pulse (HIGH state) will have a duration of
# (1 / 100) * (20 / 100) = 0.002 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 20) / 100) = 0.008 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity.
pwm.start(20)
sleep(2)

# Change duty cycle to 6%. The pulse (HIGH state) will now have a duration of
# (1 / 100) * (6 / 100) = 0.0006 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 6) / 100) = 0.0094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity.
pwm.changeDutyCycle(2.5)
sleep(1)
pwm.changeDutyCycle(5)
sleep(1)
pwm.changeDutyCycle(7.5)
sleep(1)
pwm.changeDutyCycle(10)
sleep(1)
pwm.changeDutyCycle(12.5)
sleep(1)

# Change the frequency of the PWM pattern. The pulse (HIGH state) will now have a duration of
# (1 / 10) * (6 / 100) = 0.006 seconds, followed by a low state with a duration of
# (1 / 10) * ((100 - 6) / 100) = 0.094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity, but you may
# notice flickering.
pwm.changeFrequency(10)
sleep(2)

# Stop PWM output
pwm.stop()