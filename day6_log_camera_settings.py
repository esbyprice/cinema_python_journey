import camera_utils
from datetime import datetime

def log_camera_settings():
    ##get user input
    lux= int(input("whats the lux?"))
    motion= input("how fast are they moving")
##call camera_utils functions
    iso=camera_utils.suggest_iso(lux)
    shutter=camera_utils.shutter_for_motion(motion)
#timestamps
    now=datetime.now()
##write log

    with open ("log_settings_day6.txt", "a") as file:
        file.write(f"Logged AT: {now}\n")
        file.write(f"Iso: {iso}\n")
        file.write(f"Shutter Speed: {shutter}\n")
        file.write(f"motion:{motion}\n")
        file.write("-" * 20 + "\n")
    
    print(f"Settings logged into log_settings_day6.txt @ {now}")

if __name__ =="__main__":
    log_camera_settings()