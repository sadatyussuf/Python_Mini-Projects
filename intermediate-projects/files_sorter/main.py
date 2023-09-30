import pathlib as path
import sys
import time
# import extensions
from extensions import extensions
from rich import print

# downloads_path = path.Path.home() / "Downloads"

# # This line iterate over all items in the "downloads_path" directory
# and filter out any that are not files, creating a list of all files in the directory.
# files = [i for i in downloads_path.iterdir() if i.is_file()]
# other_folders = [i for i in downloads_path.iterdir() if i.is_dir()]


def get_command_line_args():
    time.sleep(1)
    print('---------------------------------------------------')
    print('The path should be an absolute path. eg. c/Users/user/Desktop/')
    print('---------------------------------------------------')
    time.sleep(3)
    downloads_folder = path.Path.home() / "Downloads"

    if len(sys.argv) <= 1:
        return downloads_folder
    target_folder = path.Path(sys.argv[1])

    return target_folder if target_folder.exists() else downloads_folder


def create_folders(extensions: dict, target_folder: path.Path) -> None:
    """
    The function creates folders for each item in the given dictionary of extensions if the folders do
    not already exist.

    :param extensions: The `extensions` parameter is a dictionary that contains the file extensions as
    keys and the corresponding folder names as values
    :type extensions: dict
    """
    for item in extensions:
        check_folder: path.Path = target_folder / item

        if not check_folder.exists():
            check_folder.mkdir()


def sort_files(files: list, extensions: dict, target_folder: path.Path) -> None:
    """
    Sorts files based on their file extension and moves them to the corresponding folder.

    Args:
        files (list): A list of Path objects representing the files to be sorted.
        extensions (dict): A dictionary where the keys are the names of the folders to move the files to,
            and the values are lists of file extensions that should be moved to each folder.
    """
    for file in files:
        file_format = file.suffix
        print(file_format)
        for key, value in extensions.items():
            if file_format in value:
                # create a Path object for the destination folder
                destination_folder = target_folder / key

                # use the rename() method to move the file
                file.rename(destination_folder / file.name)
                # file = destination_folder / file.name


def sort_folders(other_folders: list, extensions: dict, target_folder: path.Path) -> None:
    """
    The function takes a list of folders and a dictionary of extensions, and moves folders with names not in
    the extensions dictionary to a destination folder.

    :param other_folders: A list of folders that need to be sorted
    :type other_folders: list
    :param extensions: The `extensions` parameter is a dictionary that maps file extensions to their corresponding folders.
    For example, if you have a file with extension ".txt", the dictionary might look like this: `extensions = {".txt":
    "Text_Files"}`. This means that any file with the extension "
    :type extensions: dict
    """
    for folder in other_folders:
        folder_name = folder.name
        if folder_name not in extensions:
            # if folder_name == 'test':
            # print(folder_name)
            destination_folder = target_folder / "Other_Folders"
            folder.rename(destination_folder / folder_name)


def main(target_folder_path):
    """
    The main function creates folders based on given extensions, sorts files based on extensions, and sorts other folders
    based on extensions.
    """
    create_folders(extensions, target_folder_path)
    sort_files(files, extensions, target_folder_path)
    sort_folders(other_folders, extensions, target_folder_path)


if __name__ == "__main__":
    target_folder_path = get_command_line_args()

    files = [i for i in target_folder_path.iterdir() if i.is_file()]
    other_folders = [i for i in target_folder_path.iterdir() if i.is_dir()]

    main(target_folder_path)
    # print(other_folders)
    # create_folders(extensions)
    # sort_folders(other_folders, extensions)
