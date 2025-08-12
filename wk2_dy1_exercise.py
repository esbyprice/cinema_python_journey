from datetime import datetime
now=datetime.now()
class LightingCondition:
    def __init__(self, lux, motion):
        self.lux=lux
        self.motion=motion

    def describe(self):
        return f"Light Level: {self.lux} lux, Subject Motion: {self.motion}"
    
    def log_to_file(self, filename):
        with open (filename, "a") as file:
            file.write(f"{now}" + self.describe() + "\n")
                    
light_con = LightingCondition(1000, "fast")
print(light_con.lux)
print(light_con.motion)

print(light_con.describe())

light_con.log_to_file("wk2_dy1_log.txt")