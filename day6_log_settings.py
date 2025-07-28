import camera_utils
from datetime import datetime
now=datetime.now()

lux=int(input("what is the lux?"))
motion=input("how fast are they moving")
dof=input("How shallow do you want the depth of field")

iso = camera_utils.suggest_iso(lux)
shutter = camera_utils.shutter_for_motion(motion)
f_stop= camera_utils.aperature(dof)



with open("log_settings_day6.txt", "a") as file:
    file.write(f"Logged AT: {now}\n")
    file.write(f"Iso: {iso}\n")
    file.write(f"Shutter Speed: {shutter}\n")
    file.write(f" aperture:{f_stop}\n")
    file.write(f" motion:{motion}\n")
    file.write(f" depth of field:{dof}\n")
with open("log_settings_day6.txt", "r") as file:
        print(file.read())