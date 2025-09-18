class CameraSetting:
    def __init__(self, iso, shutter, aperture):
        self.iso = iso
        self.shutter = shutter
        self.aperture = aperture

    def describe(self):
        return f"ISO: {self.iso}, Shutter: {self.shutter}, Aperture: {self.aperture}"


    def is_bright(self):
        return self.iso <= 200
macro = CameraSetting(800, "1/125", "f5.6")

print(macro.is_bright())