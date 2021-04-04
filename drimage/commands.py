import click
from .functions import *


@click.command()
@click.argument("file_name", nargs=1, required=False, type=str)
@click.option(
    "--all",
    "-a",
    help="convert all images in current directory ",
    is_flag=True
)
def commandHandler(file_name, all):
    if file_name:
        # change only one image
        # print(file_name)
        if isImage(file_name):
            print(file_name, end="  ")
            createNewImage(file_name)
            print("Done")
        else:
            print("file '", file_name, "' not exist or is not a image!")
    elif all:
        # print("all")
        images = getImageFilesList()

        for i in range(len(images)):
            print(str(i + 1) + "  " + images[i], end="  ")
            createNewImage(images[i])
            print("Done")
    else:
        click.echo('please use drimage --help')
