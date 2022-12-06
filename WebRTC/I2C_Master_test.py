import smbus
import time
DEVICE_ADDR = 0x08
bus = smbus.SMBus(1)


def Send_Data(income_char):

    if income_char == '1':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
    elif income_char == '2':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x02)
    elif income_char == '3':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x03)
    elif income_char == '4':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x04)
    elif income_char == '5':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x05)
    elif income_char == '6':
        bus.write_byte_data(DEVICE_ADDR, 0x00, 0x06)
    else:
        return "input error!"
    
    return "Sent!"
    
if __name__ == "__main__":

    x = '1'
    for i in range(1, 7):
        
        print(Send_Data(x))
        time.sleep(0.5)
        x += 1