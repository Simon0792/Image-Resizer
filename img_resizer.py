'''
This module handles the resize of the images.
Written by simone onorato
for questions and support please email simon.onorato@queensu.ca
all right reserved.
'''

# import dependencies
from PIL import Image
import os



#declaring global variables
userDirectory=os.path.dirname(os.getcwd())
templateFolder='.\\templates\\'
whiteBkgd=f'{templateFolder}1600bkg.jpg'
whiteBkgdWs=f'{templateFolder}1000bkg.jpg'


def startResAmzEbay():
    myDir = os.getcwd()
    input_directory = str(input('Enter your image directory here: '))
    input_directory = f'{input_directory}\\'
    #create output directory
    outputImg=os.mkdir(f'{input_directory}\\1600px')
    outputImg=(f'{input_directory}\\1600px\\')
    for imgFile in os.listdir(input_directory):
        resizeImgAmzEby(input_directory, imgFile, outputImg)


def resizeImgAmzEby(input_directory, imgFile, outputImg):
    currentFile=(f'{input_directory}{imgFile}')
    if os.path.isfile(currentFile):
        # open images recursively
        mainImage = Image.open(currentFile)
        # Image size, in pixels. The size is given as a 2-tuple (width, height).
        #print(mainImage.size)

        # mesure algorythm
        img_size = mainImage.size
        if img_size[0] >= img_size[1]:
            side1 = 1600
            side2 = int(1600 / img_size[0] * img_size[1])
            shortSide = side2

        if img_size[0] <= img_size[1]:
            side1 = int(1600 / img_size[1] * img_size[0])
            side2 = 1600
            shortSide = side1

        # resizing image
        rszImg = mainImage.resize((side1, side2))

        # inserting image on a white squared background
        bkgd = Image.open(whiteBkgd)
        if side1 == side2:
            position = ((0), (0))
        if side1 > side2:
            position = ((0), int(800 - (shortSide / 2)))
        if side2 > side1:
            position = (int(800 - (shortSide / 2)), (0))

        bkgd.paste(rszImg, position)

        bkgd.save(f'{outputImg}{imgFile}')


def startResWebsite():
    input_directory = str(input('Enter your image directory here: '))
    input_directory = f'{input_directory}\\'
    #create output directory
    outputImg=os.mkdir(f'{input_directory}\\1000px')
    outputImg=(f'{input_directory}\\1000px\\')
    for imgFile in os.listdir(input_directory):
        resizeImgWb(input_directory, imgFile, outputImg)


def resizeImgWb(input_directory, imgFile, outputImg):
    currentFile = (f'{input_directory}{imgFile}')
    if os.path.isfile(currentFile):
        # open images recursively
        mainImage = Image.open(f'{input_directory}{imgFile}')
        # Image size, in pixels. The size is given as a 2-tuple (width, height).
        #print('original size: ', imgFile, mainImage.size)

        # mesure algorythm
        img_size = mainImage.size
        if img_size[0] >= img_size[1]:
            side1 = 1000
            side2 = int(1000 / img_size[0] * img_size[1])
            shortSide = side2

        if img_size[0] <= img_size[1]:
            side1 = int(1000 / img_size[1] * img_size[0])
            side2 = 1000
            shortSide = side1

        #print('new W: ', side1)
        #print('new H: ', side2)

        # resizing image
        rszImg = mainImage.resize((side1, side2))
        #print()

        # inserting image on a white squared background
        bkgd = Image.open(whiteBkgdWs)
        if side1 == side2:
            position = ((0), (0))
        if side1 > side2:
            position = ((0), int(500 - (shortSide / 2)))
        if side2 > side1:
            position = (int(500 - (shortSide / 2)), (0))

        bkgd.paste(rszImg, position)
        bkgd.save(f'{outputImg}website_{imgFile}')



