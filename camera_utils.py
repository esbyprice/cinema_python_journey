def suggest_iso(lux):
    if lux > 1000:
        return 500
    elif lux > 400:
        return 1250
    elif lux > 50:
        return 2500
    else:
        return "invalid"
    
def shutter_for_motion(motion):
    motion= motion.strip().lower()
    if motion == "still":
        return "1/50"
    elif motion == "slow":
        return "1/100"
    elif motion == "fast":
        return "1/1000"
    else:
        return "Invalid"
    
def aperature(dof):
    if dof == "shallow":
        return "f/2.8"
    elif dof == "medium":
        return "f/4"
    elif dof == "deep":
        return "f/8"
    else:
        return "Invalid"

