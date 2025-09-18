iso = 800
ambient_light = 200  # in lux

if ambient_light > 1000:
    print("Set ISO to 100.")
elif ambient_light > 300:
    print("Set ISO to 400.")
elif ambient_light > 50:
    print("Set ISO to 800.")
else:
    print("Set ISO to 1600.")

    
is_night = True
is_indoor = True

if is_night and is_indoor:
    print("Use a tripod and wide aperture.")
elif is_night and not is_indoor:
    print("Boost ISO and use image stabilization.")
else:
    print("Normal shooting conditions.")
