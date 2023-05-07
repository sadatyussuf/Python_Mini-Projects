import pathlib as path

import extensions

downloads_path = path.Path.home() / "Downloads"
extensions = extensions.extensions

# # This line uses a list comprehension to iterate over all items in the "downloads_path" directory
# and filter out any that are not files, creating a list of all files in the directory.
files = [i for i in downloads_path.iterdir() if i.is_file()]


def create_folders(extensions: dict):
    """
    Creates folders based on a dictionary of extensions.

    Args:
    extensions (dict):  A dictionary where keys represent
                        file extensions and values are lists of corresponding file formats.
    """
    for item in extensions:
        check_folder: path.Path = downloads_path / item

        if not check_folder.exists():
            check_folder.mkdir()


def sort_files(files: list, extensions: dict):
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
                destination_folder = downloads_path / key

                # use the rename() method to move the file
                file.rename(destination_folder / file.name)
                # file = destination_folder / file.name


def main():
    create_folders(extensions)
    sort_files(files, extensions)


if __name__ == "__main__":
    main()
