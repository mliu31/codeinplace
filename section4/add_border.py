from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    #
    pass


if __name__ == '__main__':
    main()