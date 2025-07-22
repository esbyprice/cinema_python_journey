
from fractions import Fraction

#Define paramters


ISO=input("what is the iso?")
Shutter=input("what is the shutter?")
Aperature=input("What is the f-stop?")

from datetime import datetime
now=datetime.now()
with open("camera_settings.txt", "a") as file:
    file.write(f"Logged AT: {now}\n")
    file.write("ISO:" + ISO + "\n")
    file.write("Shutter Speed:" + Shutter +"\n")
    file.write("Aperature:" + Aperature + "\n")
with open("camera_settings.txt", "r") as file:
        print(file.read())
