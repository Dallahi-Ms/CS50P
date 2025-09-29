import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    f = sys.argv[2]
    if f not in fonts:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')

s = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(s))

