import PIL
from PIL import Image


def resize(file, width, height):
    img = Image.open('../data/images/{}'.format(file))

    img = img.resize((width, height), PIL.Image.ANTIALIAS)

    img.save('../new_data/images/{}'.format(file))

    img.close()


def create_new_samples(folder, file):
    img = Image.open('../new_data/images/{}/{}'.format(folder, file))
    for i in range(30, 360, 30):
        img.rotate(i).save('../new_data/images/{}/Rotate/rotate_{}_{}'.format(folder, i, file))

    method = PIL.Image.FLIP_LEFT_RIGHT
    img.transpose(method).save('../new_data/images/{}/FlipLR/flipLR_{}'.format(folder, file))

    method = PIL.Image.FLIP_TOP_BOTTOM
    img.transpose(method).save('../new_data/images/{}/FlipTB/flipTB_{}'.format(folder, file))

    img.close()
