from datetime import datetime


class CameraSetting:
    def __init__(self, iso, shutter, aperature):
        self.iso=iso
        self.shutter=shutter
        self.aperature=aperature

    def describe(self):
        return(f"iso:{self.iso} + shutter:{self.shutter} + fstop:{self.aperature}")
    
    def log_to_file(self, filename):
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"[{now}] {self.describe()}\n")

    def exposure_rating(self):
        if self.iso >= 800:
            print("WARNING IMAGE MAY HAVE NOISE")
        else:
            print("This is acceptable noise")
        
        if self.shutter <= 60:
            print("results may have large motion blur")
        else:
            print ("results have acceptable motion blur")
        if self.aperature >= 4:
            print("you will have Out of focus background")
        else:
            print("backgroud will have some level of focus")
        
        


while True:
    print("press 1 to input settings")
    print("press 2 to quit")
    choice=input("Select An Option: ")

    if choice == "1":
        iso=int(input("enter the ISO"))
        shutter=int(input("enter shutter: 1/"))
        aperature=int(input("enter f-stop: f/"))

        rig1 = CameraSetting(iso, shutter, aperature)
        print("✅ CameraSetting object created")
        rig1.exposure_rating()
        print("✅ exposure_rating() called")
        rig1.log_to_file("log_file.txt")
        print("✅ log_to_file() called")
        print(f"settings have been logged")
        break
        
    elif choice == "2":
        print("you have quit")
        break
    else: 
        print("invalid option press 1 to choose option or 2 to quit")
        break




