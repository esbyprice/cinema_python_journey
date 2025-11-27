from datetime import datetime

class CameraSetting:
    def __init__(self, iso, shutter, aperature):
        self.iso=iso
        self.shutter=shutter
        self.aperature=aperature

    def __str__(self):
        return f"iso:{self.iso}, shutter:{self.shutter}, iris:{self.aperature}"
    

# class CameraRig:
#     def __init__(self, name):
#         self.name=name
#         self.settings = []
    
#     def add_setting(self, setting):
#         self.settings.append(setting)

#     def list_settings(self):
#         for s in self.settings:
#             print(s)
    
#s calls __str__

daylight = CameraSetting(350,1/200,2.8)
# rig1 = CameraRig("Daylight")
# rig1.add_setting(daylight)
# rig1.list_settings()


def log_to_file(self,filename):
    self=CameraSetting
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{now}] {self}\n]")

daylight.log_to_file("log_file.txt")