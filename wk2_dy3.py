class CameraSetting:
    def __init__(self, iso, shutter, aperature):
        self.iso=iso
        self.shutter=shutter
        self.aperature=aperature

    def __str__(self):
        return(f'iso:{self.iso} + shutter:{self.shutter} + aperature:{self.aperature}')
    
    def exposure_eval(self):
        if self.iso <= 200 and self.shutter <= 1/60 and self.aperature >= 5.6:
            print("Only use in sunny areas")
        elif self.iso <=800 and self.shutter <= 1/30 and self.aperature >=2.8:
            print("this is okay to use in studio lighting conditions")
        else:
            print ("you better have a night exterior shoot running...")

    
class CameraRig:
    def __init__(self, name):
        self.name=name
        self.settings = []
    
    def add_setting(self, setting):
        self.settings.append(setting)
#confused how list_settings and summarize are working why cant i just put print(f'{self.name}+{self.setting)})
    def list_settings(self):
        for s in self.settings:
            print(s)
    
    def summarize(self):
        print(f"{self.name}")
        for setting in self.settings:
            print(setting)


setting1=CameraSetting(100, 1/1000, 2)
setting2=CameraSetting(2500,1/400, 16)
rig1=CameraRig("Sunny")
rig2=CameraRig("Real HIGH ISO")
rig1.add_setting(setting1)
rig2.add_setting(setting2)

rig1.summarize()
rig2.summarize()