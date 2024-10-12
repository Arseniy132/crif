import PIL
from PIL import Image
import struct
def crif_png(crif, png):
    try:
        with open(crif + ".crif", "rb") as f:
            width, height = struct.unpack("II", f.read(8))
            img = Image.new("RGBA", (width, height))
            pixel_data = []
            for _ in range(width * height):
                r, g, b, a = struct.unpack("BBBB", f.read(4))
                pixel_data.append((r, g, b, a))
            img.putdata(pixel_data)
            img.save(png + ".png")
            print(f"Converted {crif}.crif to {png}.png!")
    except PIL.UnidentifiedImageError or FileNotFoundError or FileExistsError or NotADirectoryError:
        print(
            f"An error occurred while converting {crif} to {png}!\nTry to use a valid .CRIF file!\nIf you already have a file called {png}.png, the choose another name for it!")

crif_in = str(input("Path of the .CRIF file without the .crif: "))
png_in = str(input("Name of the .PNG file also without extension: "))
crif_png(crif_in, png_in)