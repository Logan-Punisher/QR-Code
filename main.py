
import qrcode
img = qrcode.make()
type(img)  
img.save("Saurabh Jain-QR.png")

# animated_qrcode.py


import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://github.com/Saurabh234567/python")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)
save("animated_qrcode.gif")
