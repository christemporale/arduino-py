import pyfirmata2
import sys

def get_board(port):
    try:
        print("Initializing... ", end='', flush=True)
        board = pyfirmata2.Arduino(port)
        print("Arduino ready")
        return board
    except Exception as e:
        print ('{}\nNo Arduino found.'.format(e))
        sys.exit()


def init_pins_dig_out(board):
    dig_pins = {}
    try:
        print("Initializing pins... ")
        for pin in range(2,14):
            print("init pin {}".format(pin))
            dig_pins[pin] = board.get_pin("d:{}:o".format(pin))
        print("ready")
        return dig_pins
    except Exception as e:
        print ("Error: {}".format(e))
        sys.exit()
