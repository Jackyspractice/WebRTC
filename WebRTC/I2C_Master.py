from pyA20.i2c import i2c
import time

class PMW:

    def __init__(self) -> None:
        pass

    def initial(self):
        i2c.init("/dev/i2c-2")  #Initialize module to use /dev/i2c-2
        i2c.open(0x55)  #The slave device address is 0x55

    def send_Meg(self, num_char):

        self.initial()

        print("Start sending ", num_char)

        #If we want to write to some register
        i2c.write([0xAA, num_char]) #Write 0x20 to register 0xAA

        #i2c.write([0xAA, 0x10, 0x11, 0x12]) #Do continuous write with start address 0xAA

        i2c.close() #End communication with slave device

    def wait_for_success(self):

        self.initial()

        #If we want to do write and read
        i2c.write([0xAA])   #Set address at 0xAA register
        value = None

        while(value == None):
            value = i2c.read(1) #Read 1 byte with start address 0xAA

        print("Revieve:", value)

if __name__ == "__main__":

    pwm = PWM()

    pwm.send_Meg('1')

    pwm.wait_for_success()

    print("End")