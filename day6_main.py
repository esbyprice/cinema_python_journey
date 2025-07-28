import camera_utils

lux=int(input("what is the lux?"))
motion=input("how fast are they moving")
dof=input("How shallow do you want the depth of field")

iso = camera_utils.suggest_iso(lux)
shutter = camera_utils.shutter_for_motion(motion)
f_stop= camera_utils.aperature(dof)

print(f"shoot at this iso: {iso}")
print(f"shoot at this shutter speed: {shutter}")
print(f"use this f-stop: {f_stop}")