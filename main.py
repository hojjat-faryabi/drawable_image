from functions import *

if __name__ == '__main__':
    # get images file
    images = getImageFilesList()

    for i in range(len(images)):
        print(str(i + 1) + "  " + images[i], end="  ")
        createNewImage(images[i])
        print("Done")
