from fractions import Fraction
#Variables
ISO = 500
shutter_speed = Fraction(1,48)
is_daytime=False

#Output
print("ISO:", ISO)
print("Shutter:", shutter_speed)

#Arithmetic
NEW_ISO = ISO + 5
print("New ISO:", NEW_ISO)
if is_daytime:
    print("Put on ND")
else:
    print("shoot wide open")



#variables
ISO = 500
Shutter_speed= Fraction(1,48)
is_daytime=True

#output
print("ISO", ISO)
print("Shutter", Shutter_speed)

#calculations
if is_daytime:
    print("it IS daytime")
else:
    print("It is NOT daytime")
