import os, PIL.Image, time
intro = PIL.Image.open("intro.gif")
for i in range(intro.n_frames):
    intro.seek(i)
    frame = intro.convert("RGB")
    frame = frame.resize((os.get_terminal_size().columns, os.get_terminal_size().lines-1), PIL.Image.NEAREST)
    os.system("clear")
    for y in range(os.get_terminal_size().lines-1):
        line = ""
        for x in range(os.get_terminal_size().columns):
            r, g, b = frame.getpixel((x, y))
            color = 16 + (r * 6 // 256) * 36 + (g * 6 // 256) * 6 + b * 6 // 256
            line += "\x1b[48;5;{}m ".format(color)
        print(line)
    time.sleep(0.1)
os.system("clear")