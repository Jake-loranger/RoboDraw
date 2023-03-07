import utime
from servo import Servo
from numpad import scanKeys
 
s1 = Servo(0)       # Servo pin is connected to GP0
s2 = Servo(1)
 
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 

def servo_Angle(servo,angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    servo.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    

s1_angle = 30
s2_angle = 10

while True:
    
    direct = scanKeys()
    
    if direct == 1:
        s1_angle += 1
    if direct == 2:
        s1_angle -= 1
    if direct == 4:
        s2_angle += 1
    if direct == 5:
        s2_angle -= 1
        
    #print(direct)
        
    servo_Angle(s1, s1_angle)
    servo_Angle(s2, s2_angle) 
    
    utime.sleep(.01)
        
