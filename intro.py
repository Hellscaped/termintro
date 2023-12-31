import os, introcompiler, time, random
intro = introcompiler.compile("uncompiled/"+random.choice(os.listdir("uncompiled")))
for frame in intro["frames"]:
    print(frame[0], end="")
    time.sleep(frame[1]/1000)