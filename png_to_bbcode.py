from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def write_image_text(file_path):
    bbcode = ""

    img = Image.open(file_path)
    pixel_map = img.load()

    current_rgb = pixel_map[0, 0]
    r, g, b, a = current_rgb
    bbcode += "[color=" + rgb2hex(r, g, b) + "]"
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if current_rgb == pixel_map[x, y]:
                bbcode += "██" 
            else:
                current_rgb = pixel_map[x, y]
                r, g, b, a = current_rgb
                bbcode += "[/color][color=" + rgb2hex(r, g, b) + "]" + "██"
        bbcode += "\n"

    bbcode += "[/color]"

    with open("bbcode_output.txt", "w", encoding="utf-16") as f:
        f.write(bbcode)

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def process():
    Tk().withdraw()
    filename = askopenfilename()
    write_image_text(filename)
    print(filename)

process()
