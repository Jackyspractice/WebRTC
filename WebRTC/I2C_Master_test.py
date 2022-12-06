import smbus
DEVICE_ADDR = 0x30
bus = smbus.SMBus(4)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)