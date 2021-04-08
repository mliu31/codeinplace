"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for c in range(N_COLS):
        for r in range(N_ROWS):
            #choose_color(c,r)--didn't work? how come c and r don't pass in as variables?
            if c == 0 and r == 0:
                # pink
                patch = make_recolored_patch(1.5, 0, 1.5)
            if c == 0 and r == 1:
                # yellow
                patch = make_recolored_patch(1.5, 1.5, 0)
            if c == 1 and r == 0:
                # green
                patch = make_recolored_patch(0, 1.5, 0)
            if c == 1 and r == 1:
                # normal
                patch = make_recolored_patch(1, 1, 1)
            if c == 2 and r == 0:
                # normal
                patch = make_recolored_patch(1.5, 1.5, 1.5)
            if c == 2 and r == 1:
                # blue
                patch = make_recolored_patch(0.2, 0.2, 1.5)


            for x in range(PATCH_SIZE):
                for y in range(PATCH_SIZE):


                    location = patch.get_pixel(x, y)
                    final_image.set_pixel(x + c * PATCH_SIZE, y + r * PATCH_SIZE, location)

    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale

    return patch


if __name__ == '__main__':
    main()