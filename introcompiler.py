import os, PIL.Image, sys
if not os.path.exists("intros"):
    os.mkdir("intros")
def compile(intro):
    intro = PIL.Image.open(intro)
    introfile = ""
    for i in range(intro.n_frames):
        # add clear
        introfile += "\033c"
        intro.seek(i)
        frame = intro.convert("RGB").resize((os.get_terminal_size().columns, os.get_terminal_size().lines-1), PIL.Image.NEAREST)
        f = ""
        for y in range(os.get_terminal_size().lines-1):
            line = ""
            for x in range(os.get_terminal_size().columns):
                r, g, b = frame.getpixel((x, y))
                line += "\x1b[48;5;{}m ".format(16 + (r * 6 // 256) * 36 + (g * 6 // 256) * 6 + b * 6 // 256)
            f += line + "\n"
        introfile += f
    return introfile + "\033c"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[2], "w") as f:
            f.write(compile(sys.argv[1]))
            f.close()
    else:
        for intro in os.listdir("uncompiled"):        
            with open("compiled/"+intro, "w") as f:
                f.write(compile("uncompiled/"+intro))
                f.close()