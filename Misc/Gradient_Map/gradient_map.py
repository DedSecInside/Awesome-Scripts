import argparse
import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def apply_colormap(img_path, colors, output):
    """
    Apply a colormap to an rgb image.

    Args:
        img_path: (str): write your description
        colors: (str): write your description
        output: (todo): write your description
    """
    input_img = cv2.imread(img_path, 0)

    rgb_colors = []
    for c in colors:
        rgb_colors.append(hex_to_rgb(c))

    cmap = make_cmap(rgb_colors)

    colored_image = apply_custom_colormap(input_img, cmap)
    cv2.imwrite(output, colored_image)


def hex_to_rgb(h):
    """
    Convert hexadecimal to rgb.

    Args:
        h: (str): write your description
    """
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def make_cmap(colors):
    '''
    Creates a custom color map with equaly spaced colors
    colors: Tuple containing the RGB values. Must be an int from 0 to 255.
    '''

    bit_rgb = np.linspace(0, 1, 256)
    position = np.linspace(0, 1, len(colors))

    for i in range(len(colors)):
        colors[i] = (bit_rgb[colors[i][0]],
                     bit_rgb[colors[i][1]],
                     bit_rgb[colors[i][2]])

    colors_dict = {'red': [], 'green': [], 'blue': []}
    for pos, color in zip(position, colors):
        colors_dict['red'].append((pos, color[0], color[0]))
        colors_dict['green'].append((pos, color[1], color[1]))
        colors_dict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap('custom_colormap', colors_dict, 256)
    return cmap


def apply_custom_colormap(source_image, cmap):
    """
    Apply color colors to image_image.

    Args:
        source_image: (todo): write your description
        cmap: (todo): write your description
    """
    assert source_image.dtype == np.uint8, 'must be np.uint8 image'
    # Squeeze image to turn it to black and white
    if source_image.ndim == 3:
        source_image = source_image.squeeze(-1)

    # Initialize the matplotlib color map
    sm = plt.cm.ScalarMappable(cmap=cmap)

    # Obtain linear color range
    color_range = sm.to_rgba(np.linspace(0, 1, 256))[:, 0:3]  # color range RGBA => RGB
    color_range = (color_range*255.0).astype(np.uint8)  # [0,1] => [0,255]
    color_range = np.squeeze(np.dstack(
        [color_range[:, 2], color_range[:, 1], color_range[:, 0]]), 0)  # RGB => BGR

    # Apply colormap for each channel individually
    channels = [cv2.LUT(source_image, color_range[:, i]) for i in range(3)]
    return np.dstack(channels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gradient Map')

    parser.add_argument('-i', '--image', help='Input image file. (jpg or png)', default='image.jpg')
    parser.add_argument('-o', '--output', help='Output file name. (default: image_mapped.jpg)', default='image_mapped.jpg')
    parser.add_argument('-w', '--whitecolor', help='Hexadecimal color for white. (default: #000000)', default='#000000')
    parser.add_argument('-b', '--blackcolor', help='Hexadecimal color for black. (default: #ffffff)', default='#ffffff')

    args = vars(parser.parse_args())

    apply_colormap(args['image'], [args['blackcolor'], args['whitecolor']], args['output'])
    print('Color map applied: {}'.format(args['output']))
