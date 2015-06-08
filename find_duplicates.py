from os import listdir
from os.path import isfile, join
from settings import SOURCE_DIR

def read_dir(dir_name):
    """ reads the directory for files """

    only_files = []
    only_dirs = []

    for f in listdir(dir_name):
        if isfile(join(dir_name, f)):
            only_files.append(dir_name + "/" + f)
        else:
            only_dirs.append(dir_name + "/" + f)

    print(only_files)
    print(only_dirs)


if __name__ == "__main__":
    read_dir(SOURCE_DIR)

