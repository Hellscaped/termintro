import os, PIL.Image, time
width = os.get_terminal_size().columns
height = os.get_terminal_size().lines-1
intro = PIL.Image.open("intro.gif")
for i in range(intro.n_frames):
    intro.seek(i)
    frame = intro.convert("RGB")
    frame = frame.resize((width, height), PIL.Image.NEAREST)
    os.system("clear")
    for y in range(height):
        line = ""
        for x in range(width):
            r, g, b = frame.getpixel((x, y))
            color = 16 + (r * 6 // 256) * 36 + (g * 6 // 256) * 6 + b * 6 // 256
            line += "\x1b[48;5;{}m ".format(color)
        print(line)
    time.sleep(0.1)
os.system("clear")