import logging
import serial
import os
from time import sleep
import math

Id_device = b'\x01'
Read_Device = b'\x04'

class CVM_C10:

    def __init__(self, uart="/dev/ttyS10", baud_rate=19200):

        self.logger = logging.getLogger('events.egeo_chips')
        try:
            # Timeout value set to 10 to let the port wait the necessary time for most
            # time consuming lectures
            self.port = serial.Serial(port=uart, baudrate=baud_rate, timeout=3)
        except serial.SerialException:
            self.logger.exception("Can't open the serial port. Please close any applications using the serial port and "
                                  "try again.")

    def CVM_C10_data(self, address, quantity, quantity_bytes):
        self.port.write(self.data_packet(address, quantity))
        return self.port.read(quantity_bytes)

    def data_packet(self, address, quantity):
        data = Id_device + Read_Device + address + quantity
        crc = self.crc16(data)
        LSB = (crc & 0xff00) >> 8
        MSB = (crc & 0x00ff)
        consult_data = data + bytearray([MSB, LSB])
        return consult_data

    def crc16(self, data):
        POLY = 0xa001
        crc = 0xffff
        for byte in data:
            crc = crc ^ byte
            for i in range(8):
                flag = crc & 0x0001
                if flag > 0:
                    crc = (crc >> 1) ^ POLY
                else:
                    crc = crc >> 1
        return crc

    def value_data_4B(self, data, factor):

        return int.from_bytes(data[3:7], byteorder='big', signed=True) / factor

    def value_data_2B(self, data, factor):

        return int.from_bytes(data[3:5], byteorder='big', signed=True) / factor

    def close_conection(self):
        self.port.close()
