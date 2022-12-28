import os
from PIL import Image
from varname import nameof


def resize_image(folder_name, img_file_name, output_folder):
    if not os.path.exists(output_folder):
        return

    vertical_360x640 = (360, 640)
    horizontal_640x360 = (640, 360)

    img_file_path = fr'{folder_name}\{img_file_name}'
    im = Image.open(img_file_path)

    new_img_file_name = rename_img_file(img_file_name)

    if im.width == 1500 or im.width == 1501:
        if os.stat(img_file_path).st_size >= 800000:
            save_img_w_compression(im, vertical_360x640, output_folder, new_img_file_name, nameof(vertical_360x640))
        else:
            save_img(im, vertical_360x640, output_folder, new_img_file_name, nameof(vertical_360x640))
        im.close()

    elif im.width == 2001 or im.width == 2002 or im.width == 2000:
        if os.stat(img_file_path).st_size >= 800000:
            save_img_w_compression(im, horizontal_640x360, output_folder, new_img_file_name, nameof(horizontal_640x360))
        else:
            save_img(im, horizontal_640x360, output_folder, new_img_file_name, nameof(horizontal_640x360))
        im.close()
        os.remove(fr'{folder_name}\{img_file_name}')


def rename_img_file(img_file_name):
    img_file_name = f'{img_file_name}'
    return img_file_name.removesuffix('.jpg').removesuffix('.png').replace(' ', '_').lower()


def save_img(im, resize_dimension, output_folder, new_img_file_name, nameof_dimension):
    im.resize(resize_dimension).convert('RGB').save(fr'{output_folder}\{new_img_file_name}_'fr'{nameof_dimension}.png',
                                                    'PNG', quality=100, subsampling=0, compress_level=0, dpi=(72, 72))


def save_img_w_compression(im, resize_dimension, output_folder, new_img_file_name, nameof_dimension):
    im.resize(resize_dimension).convert('RGB').save(fr'{output_folder}\{new_img_file_name}_'fr'{nameof_dimension}.png',
                                                    'PNG', quality=100, subsampling=0, compress_level=1, dpi=(72, 72))
