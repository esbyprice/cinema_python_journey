from datetime import datetime
now=datetime.now()
class CameraSetting:
    def __init__(self, iso, shutter, aperture):
        self.iso=iso
        self.shutter=shutter
        self.aperture=aperture
    
    def describe(self):
        return f"iso:{self.iso}, ss: {self.shutter}, iris: {self.aperture}"
    
class CameraRig:
    def __init__(self, name):
        self.name=name
        self.settings=[] 
    
    def add_setting(self, setting):
        self.settings.append(setting)

    def list_settings(self):
        for s in self.settings:
            print(s.describe())

    def save_rig(self):
        with open("wk2_dy2_log.txt", "a") as file:
            file.write(f"{now}" + {CameraRig.settings} + "\n") 


macro=CameraSetting(412300,"1/23200", "f/2.23238")
studio=CameraSetting(800,"1/400", "f/4")

rig1=CameraRig("Macro")
rig1.add_setting(macro)
rig1.save_rig()
rig1.list_settings()