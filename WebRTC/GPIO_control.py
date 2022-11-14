
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
Box_GPIO_port = ["PA1", "PA0", "PA3", "PA7", "PA19", "PA18"] #11, 13, 15, 12, 16, 18


def initial():
    gpio.init()
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

def high(which_box):
    global Box_GPIO_port

    which_box = int(which_box)

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

def low(which_box):
    global Box_GPIO_port

    which_box = int(which_box)

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

if __name__ == "__main__":

    initial()
    print("high all")
    high("1")
    high("2")
    high("3")
    high("4")
    high("5")
    high("6")
    print("sleep 5s")
    sleep(5)