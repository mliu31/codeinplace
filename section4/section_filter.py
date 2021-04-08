from simpleimage import SimpleImage


def main():
    """
    This program loads an image and applies the narok filter
    to it by setting "bright" pixels to grayscale values.
    """
    image = SimpleImage('images/simba-sq.jpg')

    # visit every pixel (for loop)
    for pixel in image:
        # find the average
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # if average > "bright"
        if average > 153:
            # set this pixel to grayscale
            pixel.red = average
            pixel.green = average
            pixel.blue = average

    image.show()


if __name__ == '__main__':
    main()