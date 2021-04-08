from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trime_size pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trime_size is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trime_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trime_size pixels shaved off each
        side of the original image
    """
    new_width = original_img.width - 2 * trim_size
    new_height = original_img.height - 2 * trim_size
    new_img = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            old_x = x + trim_size
            old_y = y + trim_size
            orig_pixel = original_img.get_pixel(old_x, old_y)
            new_img.set_pixel(x, y, orig_pixel)

    return new_img


if __name__ == '__main__':
    main()