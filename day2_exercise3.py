#ask for motion information

subject_motion= input("Is your subject still, slow, or fast").lower()

#make suggestion
if subject_motion == "still":
    print("use 1/60 or slower")
elif subject_motion == "slow":
    print("use 1/100 or 1/200")
elif subject_motion == "fast":
    print("use 1/500 or 1/1000")
else:
    print("invalid please write still, slow, or fast")