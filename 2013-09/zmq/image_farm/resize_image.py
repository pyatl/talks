import os
from StringIO import StringIO

from PIL import Image


def format_output_filename(input_filename, max_height):
    base, extension = os.path.splitext(input_filename)
    output_filename = ''.join([base, '_thumbnail', str(max_height), extension])

    return output_filename


def resize_image(image_data, max_height, output_filename):
    size = max_height, max_height

    image = Image.open(StringIO(image_data))
    image.thumbnail(size, Image.ANTIALIAS)

    image.save(output_filename)

    return image


# test code that can be run standalone from the command line

if __name__ == '__main__':
    import sys

    max_height = 128
    input_filename = sys.argv[1]

    output_filename = format_output_filename(input_filename, max_height)

    with open(input_filename, 'rb') as f:
        image_data = f.read()

    image = resize_image(image_data, max_height, output_filename)

    print 'Resized {} ({} {} {})'.format(
        input_filename, image.format, image.size, image.mode)
