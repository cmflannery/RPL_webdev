from PIL import Image


size = 800, 800
fileName = "VickieTroung.jpg"
img = Image.open(fileName)
imgCropped = img.crop((964, 0, 4420, 3456))
imgCropped.thumbnail(size, Image.ANTIALIAS)
newName = 'CROPPED' + fileName
imgCropped.save(newName)
