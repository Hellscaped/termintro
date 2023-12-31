import os, sys,time
with open(sys.argv[1], "r") as f:
    intro = f.read()
    intro = intro.split("\033c")
    f.close()
for frame in intro:
    print("\033c", end="")
    print(frame, end="")
    time.sleep(0.1)
print("\033c", end="")