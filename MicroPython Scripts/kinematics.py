import math


def inverseKinematic(x, y):
    a2 = 4.5 #inches - preliminary
    a4 = 3.5 #inches - preliminary
    
    if x == 0:
        theta1 = 180
    else: 
        #Equation 1
        r = (x**2) + (y**2)
        
        #Equation 2
        phi1 = math.acos((((a4**2)-(a2**2)-(r**2))/(-2*a2*r)))
        phi1 = phi1*(180/math.pi)
        
        #Equation 3
        phi2 = math.atan(y/x)
        phi2 = phi2*(180/math.pi)
        
        #Equation 4
        theta1 = phi2 - phi1
        
        #Equation 5
        phi3 = math.acos((((r**2)-(a2**2)-(a4**2))/(-2*a2*a4)))
        phi3 = phi3*(180/math.pi)
        
        #Equation 6
        theta2 = 180 - phi3
        
        print(theta1)
        
        if y < 0:
            theta1 = theta1 * -1
    
    
    return theta1

