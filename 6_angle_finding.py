'''Write a program to find the third angle of a triangle
if two angles are given. '''

'''def third_angle(angle1, angle2):
   
    angle3 = 180-(angle1+angle2)
    return angle3

first_angle = float(input("first angle: "))
second_angle = float(input("Second angle: "))

Third_angle = third_angle(first_angle, second_angle)
print(Third_angle)'''



def third_angle(angle1, angle2):
    if (angle1>0 and angle2>0) and(angle1+ angle2)<180:
        angle3 = 180-(angle1+angle2)
        return angle3

    else:
        print("the angle is not right")


        
   
first_angle = float(input("first angle: "))
second_angle = float(input("Second angle: "))

Third_angle = third_angle(first_angle, second_angle)
print(Third_angle)

