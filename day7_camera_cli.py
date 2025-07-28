import camera_utils
from datetime import datetime

def get_user_input():
    try:
        lux = int(input("Enter light level in lux: "))
        motion = input("Enter subject motion (still, slow, fast): ")
        dof = input("Enter depth of field (shallow, medium, deep): ")
        return lux, motion, dof
    except ValueError:
        print("❌ Invalid input. Please enter numbers for lux.")
        return None, None, None

def log_settings(iso, shutter, aperture, lux, motion, dof):
    now = datetime.now()
    with open("camera_log.txt", "a") as file:
        file.write(f"Logged at: {now}\n")
        file.write(f"Light: {lux} lux | Motion: {motion} | DoF: {dof}\n")
        file.write(f"ISO: {iso} | Shutter: {shutter} | Aperture: {aperture}\n")
        file.write("-" * 30 + "\n")

def run():
    lux, motion, dof = get_user_input()
    if lux is None:
        return

    iso = camera_utils.suggest_iso(lux)
    shutter = camera_utils.shutter_for_motion(motion)
    aperture = camera_utils.aperature(dof)

    print("\n📷 Recommended Camera Settings:")
    print(f"ISO: {iso}")
    print(f"Shutter Speed: {shutter}")
    print(f"Aperture: {aperture}")

    log_settings(iso, shutter, aperture, lux, motion, dof)

if __name__ == "__main__":
    run()
