from wk2_dy3 import CameraSetting, CameraRig


if __name__ == "__main__":

    setting1=CameraSetting(100, 1/1000, 2)
    setting2=CameraSetting(2500,1/400, 16)
    rig1=CameraRig("Sunny")
    rig2=CameraRig("Real HIGH ISO")
    rig1.add_setting(setting1)
    rig2.add_setting(setting2)

    rig1.summarize()
    rig2.summarize()
    print(__name__)

