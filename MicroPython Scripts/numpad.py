from machine import Pin
import utime
import time

def scanKeys():

    # Create a map of buttons

    matrix_keys = [['1','2','3', 'A'],
                   ['4','5','6', 'B'],
                   ['7','8','9', 'C'],
                   ['*','0','#', 'D']]

    # Coordinate Rows and columns with Pin #s
                   
    keypad_rows = [2, 3, 4, 5]
    keypad_columns = [6, 7, 8, 9]

    col_pins = []
    row_pins = []

    # Assign GPIO Pins and setup input/output
    for x in range(0,4):
        row_pins.append(Pin(keypad_rows[x],Pin.OUT))
        row_pins[x].value(1)
        col_pins.append(Pin(keypad_columns[x],Pin.IN, Pin.PULL_DOWN))
        col_pins[x].value(0)
        


    key_press = None
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            key = None
                
            if col_pins[col].value() == 1:
                key_press = int(matrix_keys[row][col])
                #print(matrix_keys[row][col])
        row_pins[row].low()
        
    return key_press

