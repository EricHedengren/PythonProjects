from pyfirmata import Arduino, util
import time

board = Arduino('COM8')
board.digital[10].write(1)
time.sleep(5)
board.digital[10].write(0)