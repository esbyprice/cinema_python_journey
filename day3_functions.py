


def suggest_iso(light_level):
    if light_level > 1000:
        return 100
    elif light_level > 300:
        return 500
    elif light_level > 50:
        return 800
    else:
        return 1600

#call function

try:
    light=int(input("What is th light lux?"))
    print("ISO:", suggest_iso(light))
except ValueError:
    print("You need to put in a number")