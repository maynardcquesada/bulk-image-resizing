import FolderFunctions as Folder
import ImageFunctions as ImageFunc

if __name__ == '__main__':
    var_folder_name = input(r'Input Image folder: ')
    var_output_folder_name = input(r'Input Output Folder: ')

    for img_file in Folder.get_folder_images(var_folder_name):
        ImageFunc.resize_image(var_folder_name, img_file, var_output_folder_name)
