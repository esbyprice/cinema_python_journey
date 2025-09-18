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
            file.write 


macro=CameraSetting(400,"1/200", "f/2.8")
studio=CameraSetting(800,"1/400", "f/4")

rig1=CameraRig("Macro")
rig1.add_setting(macro)
rig1.add_setting(studio)
rig1.list_settings()