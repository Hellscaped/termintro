import os, introcompiler, time, random
intro = introcompiler.compile("uncompiled/"+random.choice(os.listdir("uncompiled")))
intro = intro.split("\033c")
for frame in intro:
    print("\033c", end="")
    print(frame, end="")
    time.sleep(0.1)
print("\033c", end="")