import sys
import time
import pyfirmata2

port = '/dev/ttyACM0'

leonardo = {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(6)),
        'pwm': (3, 5, 6, 9, 10, 11, 13),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
       }


try:
   print("Initializing... ", end = '', flush=True)
   #board = pyfirmata2.Board(port, leonardo) 
   board = pyfirmata2.Arduino(port) 
   print("Ready")
except:
   print ('No Arduino found')
   sys.exit()

dig_pin = {}

try:
   print("Initializing pins... ")
   for pin in [3, 5, 6, 9, 10, 11]:
      print("init pin {}".format(pin))
      dig_pin[pin] = board.get_pin("d:{}:o".format(pin))

   for pin in [2, 4, 7, 8, 12, 13]:
      print("init pin {}".format(pin))
      dig_pin[pin] = board.get_pin("d:{}:o".format(pin))

   print("ready")
except Exception as e:
   print ("Error: {}".format(e))
   sys.exit()



while True:
    in_txt = input ("command ")
    num, on_off = in_txt.split(" ")
    print("led {} {}".format(num, on_off))    
    dig_pin[int(num)].write(float(on_off))

# 4, 8, 12: non funziona, tensione bassissima
# 5 tensione di .25 anziché .29

# msg = bytearray([ANALOG_MESSAGE + self.pin_number, value % 128, value >> 7])


#for num in range(2, 14):
#    print("pin {}...".format(num))
#    dig_pin[num].write(1)
#    time.sleep(2)
#    dig_pin[num].write(0)    


