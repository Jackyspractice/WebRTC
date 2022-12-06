import smbus
import time
DEVICE_ADDR = 0x09
bus = smbus.SMBus(1)


def Send_Data(income_char):

    if income_char == '1':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x31)
    elif income_char == '2':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x32)
    elif income_char == '3':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x33)
    elif income_char == '4':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x34)
    elif income_char == '5':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x35)
    elif income_char == '6':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x36)
    else:
        return "input error!"
    
    return "Sent!"
    
if __name__ == "__main__":

    for i in range(1, 7):
        
        print(Send_Data(str(i)))
        time.sleep(0.5)