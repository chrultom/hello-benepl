import serial
from time import sleep
from binascii import unhexlify
from sys import argv


def com10target(which_side):
    ser = serial.Serial(port='COM10', baudrate=9600, bytesize=8)
    ser.write(unhexlify(which_side))
    sleep(0.5)
    ser.flush()
    sleep(0.5)
    ser.close()

try:
    if argv[1] == "80" or argv[1] == "83":
        com10target(argv[1])
    else:
        print ("You have to put 80 or 83 as parameter!")
except IndexError:
    print ("Wrong number of parameters!")
