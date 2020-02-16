import sys
import time
import pyfirmata

leonardo_port = '/dev/ttyACM0'

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    print("Initializing... ", end = '', flush=True)
    board = pyfirmata.Arduino(leonardo_port)
    print("ready")
except:
    print ('No Arduino found')
    sys.exit()


dig_5 = board.get_pin("d:5:p")
dig_5.write(1)

ana_0 = board.get_pin('a:0:i')
thread = pyfirmata.util.Iterator(board)
thread.start()
#board.analog[0].enable_reporting()

while True:
    adc_val = ana_0.read()
    if adc_val:
        volts = map(adc_val, 0, 1, 0, 5)
        print("val ADC: {} = {} volts".format(adc_val, volts))
        dig_5.write(adc_val)
    else:
        print("Nothing!")
    time.sleep(0.5)





