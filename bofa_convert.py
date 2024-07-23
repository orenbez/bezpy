import os
from glob import glob
from shutil import copy2, rmtree
from zipfile import ZipFile


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths

if __name__ == '__main__':

    output_path = 'C:\\Temp\\Bofa'

    # clean-up
    if os.path.exists(output_path):
        rmtree(output_path)
    os.mkdir(output_path)

    sql = glob(f"./**/*.sql", recursive=True)
    py = glob(f"./**/bez*.py", recursive=True)
    full = sql + py

    zip_file = 'C:\\Temp\\bofa.zip'

    for file in full:
        output_location = output_path + file[file.rfind('\\'):] + '.txt'
        print(output_location)
        copy2(file, output_location)

    with ZipFile(zip_file, 'w') as zip:
        files_to_zip = get_all_file_paths(output_path)
        for file in files_to_zip:
            zip.write(file)

    print('Created', zip_file)
