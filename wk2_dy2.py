from datetime import datetime

class CameraSetting:
    def __init__(self, iso, shutter, aperature):
        self.iso=iso
        self.shutter=shutter
        self.aperature=aperature

    def describe(self):
        return f"iso:{self.iso}, shutter:{self.shutter}, iris:{self.aperature}"
    

class CameraRig:
    def __init__(self, name):
        self.name=name
        self.settings = []
    
    def add_setting(self, setting):
        self.settings.append(setting)

    def list_settings(self):
        for s in self.settings:
            print(s.describe())
    
    def log_to_file(self,filename):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"[{now}] {self.describe()}\n]")

daylight = CameraSetting(200,1/60,2.8)
rig1 = CameraRig("Daylight")
rig1.add_setting(daylight)
rig1.list_settings()
rig1.log_to_file(daylight, "log_file.txt")