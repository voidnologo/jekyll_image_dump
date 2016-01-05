import os


def renumber_file_names(path, destination=None, start_idx=0):
    dest_path = destination or path
    for idx, test_file in enumerate(os.listdir(path), start=start_idx):
        source = os.path.join(path, test_file)
        dest = os.path.join(dest_path, '{}{}'.format(idx, os.path.splitext(test_file)[1]))
        os.renames(source, dest)
