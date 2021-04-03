from PIL import Image
import os
import pathlib
from constants import *


def calcDP(px):
    index = -1
    if px in SIZES_PX:
        index = SIZES_PX.index(px)
    else:
        for item in SIZES_PX:
            if item > px:
                index = SIZES_PX.index(item)
                break

    if index == -1:
        index = len(SIZES_PX) - 1

    return px / (SIZES_DPI[index] / 160)


def calcNewSizes(dp):
    res = []
    for item in SCALING:
        res.append(int(item * dp))
    return res


def getImageFilesList():
    files = []
    for file in os.listdir("."):
        if isImage(file):
            files.append(file)
    return files


def isImage(name):
    if os.path.isfile(name):
        file_parts = pathlib.Path(name)
        if file_parts.suffix.removeprefix(".") in SUPPORTED_FORMATS:
            return True
    return False


def checkImageNameForSave(name: str):
    # in android drawables images can't start with numbers
    # and is better they haven't capitalize words
    name = name.lower()

    if name[0].isnumeric():
        name = '_' + name

    return name


def createNewImage(img_path):
    img = Image.open(img_path)
    x, y = img.size
    ratio = x / y

    new_xs = calcNewSizes(calcDP(x))
    new_ys = []
    for item in new_xs:
        new_ys.append(int(item / ratio))

    for i in range(len(SCALING)):
        root = "Drawable"
        folder = "drawable-" + DRAWABLE_SIZE_NAMES[i]
        name = checkImageNameForSave(img_path)
        path = os.path.join(root, folder, name)

        try:
            pathlib.Path(os.path.join(root, folder)).mkdir(parents=True, exist_ok=True)
            new_img = img.resize((new_xs[i], new_ys[i]))
            new_img.save(checkImageNameForSave(path))
        except Exception as ex:
            print(ex)
