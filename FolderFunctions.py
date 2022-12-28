import os


def get_folder_images(folder_name):
    img_list = []

    if not os.path.exists(folder_name):
        return

    img_files = os.listdir(folder_name)
    extensions = ['jpg', 'jpeg', 'png', 'gif']

    for img_file in img_files:
        ext = img_file.split('.')[-1]

        if ext in extensions:
            img_list.append(img_file)

    return img_list
