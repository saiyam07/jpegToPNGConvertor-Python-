import os
import sys
from PIL import Image


def createDestinationFolder(destinationFolder):
        os.mkdir(destinationFolder)

def convertImages(sourceDir , destDir):
    for img in os.listdir(sourceDir):
        if '.jpeg' in img or '.jpg' in img:
            imageFile = Image.open(f'{sourceDir}/{img}')
            #get the file name
            newName = os.path.splitext(img)
            #save the .png file in the destination folder
            imageFile.save(f'{destDir}/{newName[0]}.png')


sourceFolderDir = sys.argv[1]

destinationFolderDir = sys.argv[2]

if not(os.path.exists(destinationFolderDir)) :
    createDestinationFolder(destinationFolderDir)


convertImages(sourceFolderDir,destinationFolderDir)