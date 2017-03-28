from PIL import Image


size = 600, 450
for i in range(1595,1622):
    fileBase = 'IMG_'
    fileName = fileBase + str(i) + '.jpg'
    img = Image.open(fileName)
    imgCropped = img.crop((964, 0, 4420, 3456))
    imgCropped.thumbnail(size, Image.ANTIALIAS)
    newName = 'CROPPED' + fileName
    imgCropped.save(newName)
    
