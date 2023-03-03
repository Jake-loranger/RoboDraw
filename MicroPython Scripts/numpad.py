from machine import Pin
import utime

# Create a map of buttons

matrix_keys = [['1','2','3', 'A'],
               ['4','5','6', 'B'],
               ['7','8','9', 'C'],
               ['*','0','#', 'D']]

# Coordinate Rows and columns with Pin #s
               
keypad_rows = [9, 10, 11, 12]
keypad_columns = [14, 15, 16, 17]

col_pins = []
row_pins = []

# Assign GPIO Pins and setup input/output
for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x],Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x],Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    

def scanKeys():
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            key = None
            
            if col_pins[col].value() == 1:
                print("you have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                utime.sleep(0.3)
        row_pins[row].low()
        
while True:
    scanKeys()
