# commit message help


def exposure_value(shutter, aperature, ISO):
    try:
        ev = (aperature ** 2) / shutter * (100 / ISO)
        return round(ev,2)
    except Exception as e:
        return f"Error: {e}"
print(exposure_value(1/125, 2.8, 250))