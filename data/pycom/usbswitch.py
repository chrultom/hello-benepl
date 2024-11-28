import serial
import time
import binascii


def com1():
    ser = serial.Serial(port='COM1', baudrate=115200, bytesize=8)

    print (ser.name)
    ser.write('root\r\n')
    time.sleep(2)
    #ser.write("mount - / -oremount, rw\r\n")
    #time.sleep(2)
    ser.write('touch dupa\r\n')
    time.sleep(2)
    ser.close()


def com10target(which_side):
    ser = serial.Serial(port='COM10', baudrate=9600, bytesize=8)
    ser.write(binascii.unhexlify(which_side))
    time.sleep(0.5)
    ser.flush()
    time.sleep(0.5)
    ser.close()

#com1()
x = input("Do (c)ompa czy do (t)argeta?")
if x == "c":
    com10target("80")
else:
    com10target("83")

#83 = 1010011, 10000000
#80 = 1010000, 10000011
