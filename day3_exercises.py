from fractions import Fraction

def shutter_speed_for_motion(speed):
    if speed == "still":
        return Fraction (1,60)
    elif speed == "slow":
        return Fraction (1,250)
    elif speed == "fast":
        return Fraction (1,500)
    else:
        raise ValueError("Invalid input: must be still slow fast")
    
try:
    subject_speed=input("What is the subject motion?").lower()
    result = shutter_speed_for_motion(subject_speed)
    print("Set shutter to:", result)
except Exception as ve:
    print("⚠️", ve)
