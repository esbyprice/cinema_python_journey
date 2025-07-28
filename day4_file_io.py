# Open a file for writing ('w' overwrites if it exists)
file = open("camera_log.txt", "w")
file.write("Log Start\n")
file.write("ISO: 400\n")
file.close()

file = open("camera_log.txt", "a")
file.write("Shutter Speed: 1/125\n")
file.close()
