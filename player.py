import os, sys,time, json
with open(sys.argv[1]) as f:
    intro = json.loads(f.read())
    f.close()
for frame in intro["frames"]:
    print(frame[0], end="")
    time.sleep(frame[1]/1000)