from datetime import datetime

class CameraSetting:
    def __init__(self, iso, shutter, aperature):
        self.iso=iso
        self.shutter=shutter
        self.aperature=aperature

    def describe(self):
        return f"iso:{self.iso}, shutter:{self.shutter}, iris:{self.aperature}"
    
    def log_to_file(self,log_file.txt):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file.txt, "a") as file:
            file.write(f"[{now}] {self.describe()}\n]")
    
        

try: 
    iso=int(input("enter iso:"))
except ValueError:
    print("must be number, IDIOT!")

try:
    shutter=str(input("enter shutter pls")).lower()
except ValueError:
    print("must be f string")

try:
    aperature=str(input("what is iris???")).lower()
except ValueError:
    print("must be string")



user_settings=CameraSetting(iso, aperature, shutter)

user_settings.log_to_file("log_file.txt")

print("settings have been muthafuckin logged BIATCH")