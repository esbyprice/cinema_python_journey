


class cameraSettings:
    def __init__(self, WB, codec, resolution, density):
     self.WB=WB
     self.codec=codec
     self.resolution=resolution
     self.density=density

    def describe(self):
        return f"WB:{self.WB} | codec:{self.codec} | resolion:{self.resolution}"
        
    def destiny_distro(density):
      if cameraSettings.codec == "ZRAW":
        density="density1"
      else:
         density="density2"

    codec=input("what is the codec? ZRAW or ProRes").lower()
    resolution=input("What is the resolution? 4K or 1080P").lower()
    WB=input("what is WB?").lower()
    density=""

class cameraArray:
   def __init__(self, name):
      self.name=name
      self.settings=[]

   def addSetting(self,setting):
      self.settings.append(setting)

   def listSetting(self):
      print: f"WB: {WB} | codec:{codec} | resolution: {resolution} | density:{density}"

   def saveArray(self):
      with open("camera_log.txt", "a") as file:
        file.write(cameraSettings)

array1=cameraSettings("5600K", "ZRAW", "4K", "density")
array2=cameraSettings("5600K", "prores", "1080p", "density")

set1=cameraArray("Test")
set1.listSetting()
set1.saveArray()