import PIL
from PIL import Image
import struct

def png_to_crif(png, crif):
    try:
        img = Image.open(png).convert("RGBA")
        width, height = img.size
        pixels = img.getdata()

        with open("crif.crif", "wb") as f:
            f.write(struct.pack("II", width, height))
            for pixel in pixels:
                f.write(struct.pack("BBBB", *pixel))

        print(f"Converted {png}.png to {crif}.crif!")
    except PIL.UnidentifiedImageError or FileNotFoundError or FileExistsError:
        print(f"An error occurred while converting {png} to {crif}!\nTry to use a valid .PNG file!\nIf you already have a file called {crif}.CRIF, the choose another name for it!")

png_in = str(input("Path to .PNG file without the png extension: "))
crif_in = str(input("Name of the .CRIF file also without extension: "))
png_to_crif(png_in + ".png", crif_in)
