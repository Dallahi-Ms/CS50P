import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit( "Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith('jpg'):
    sys.exit("Not a jpg file")
if not sys.argv[2].endswith('jpg'):
    sys.exit("Input and output have different extensions")

before, after = sys.argv[1], sys.argv[2]

try:
    with Image.open(before) as img:
        fitted = ImageOps.fit(img, (600, 600))
        with Image.open("shirt.png") as shirt:
            fitted.paste(shirt, (0, 0), shirt)
        fitted.save(after)

except FileNotFoundError:
    sys.exit("")
