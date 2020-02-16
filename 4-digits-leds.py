import sys
import time
import math
import pyfirmata2

port = '/dev/ttyACM0'

segmentPins = [6, 7, 8, 9, 10, 11, 12, 13]
num_digits = 4;

digitPins = [2, 3, 4, 5]

delay = .001

def clear():
    dig_pin[6].write(1)
    dig_pin[7].write(1)
    dig_pin[8].write(1)
    dig_pin[9].write(1)
    dig_pin[10].write(1)
    dig_pin[11].write(1)
    dig_pin[12].write(1)
    dig_pin[13].write(1)

def write_0():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(0)
    dig_pin[11].write(0)
    dig_pin[12].write(1)
    dig_pin[13].write(1)

def write_1():
    dig_pin[6].write(1);
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(1)
    dig_pin[10].write(1)
    dig_pin[11].write(1)
    dig_pin[12].write(1)
    dig_pin[13].write(1)

def write_2():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(1)
    dig_pin[9].write(0)
    dig_pin[10].write(0)
    dig_pin[11].write(1)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_3():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(1)
    dig_pin[11].write(1)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_4():
    dig_pin[6].write(1)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(1)
    dig_pin[10].write(1)
    dig_pin[11].write(0)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_5():
    dig_pin[6].write(0)
    dig_pin[7].write(1)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(1)
    dig_pin[11].write(0)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_6():
    dig_pin[6].write(0)
    dig_pin[7].write(1)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(0)
    dig_pin[11].write(0)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_7():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(1)
    dig_pin[10].write(1)
    dig_pin[11].write(1)
    dig_pin[12].write(1)
    dig_pin[13].write(1)

def write_8():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(0)
    dig_pin[11].write(0)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_9():
    dig_pin[6].write(0)
    dig_pin[7].write(0)
    dig_pin[8].write(0)
    dig_pin[9].write(0)
    dig_pin[10].write(1)
    dig_pin[11].write(0)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

def write_minus():
    dig_pin[6].write(1)
    dig_pin[7].write(1)
    dig_pin[8].write(1)
    dig_pin[9].write(1)
    dig_pin[10].write(1)
    dig_pin[11].write(1)
    dig_pin[12].write(0)
    dig_pin[13].write(1)

funcs = {'-': write_minus, 0: write_0, 1: write_1, 2: write_2, 3: write_3, 4: write_4,
                           5: write_5, 6: write_6, 7: write_7, 8: write_8, 9: write_9}

def show_map(pin_map):
    for pin, number in pin_map.items():
        dig_pin[pin].write(1)
        funcs[number]()
        time.sleep(delay)
        dig_pin[pin].write(0)
        clear()

def get_pin_map(n):
    if n > 9999 or n < -999:
        print("Number not supported")
        return {}
    if n == 0:
        return {digitPins[4]:0}
    pin_map = {}
    num_dig = 1+int(math.log10(abs(n)))
    #print("num digits: {}".format(num_dig))
    if n < 0:
        pin_map[digitPins[3 - num_dig]] = "-"

    for pos in range(num_dig, 0, -1):
        num = int(abs(n) % math.pow(10, pos) / math.pow(10, pos-1))
        pin = digitPins[4 - pos]
        pin_map[pin] = num

    return pin_map


def show_number(n):
    map = get_pin_map(n)
    for pin, number in map.items():
        dig_pin[pin].write(1)
        funcs[number]()
        time.sleep(delay)
        dig_pin[pin].write(0)
        clear()

try:
   print("Initializing... ", end='', flush=True)
   board = pyfirmata2.Arduino(port)
   print("ready")
except:
   print ('No Arduino found')
   sys.exit()

dig_pin = {}

try:
   print("Initializing pins... ")
   for pin in range(2,14):
      print("init pin {}".format(pin))
      dig_pin[pin] = board.get_pin("d:{}:o".format(pin))
   print("ready")
except Exception as e:
   print ("Error: {}".format(e))
   sys.exit()



for k in range (1,9999):
    m = get_pin_map(k)
    for i in range(1, 3):
        show_map(m)

#while(True):
#    show_number(-42)

