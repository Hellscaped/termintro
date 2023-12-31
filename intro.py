#/usr/bin/env python3
import os, introcompiler, time, random,sys
if len(sys.argv) > 1:
    intro = introcompiler.compile(sys.argv[1])
else:
    intro = introcompiler.compile("uncompiled/"+random.choice(os.listdir("uncompiled")))
for frame in intro["frames"]:
    print(frame[0], end="")
    time.sleep(frame[1]/1000)