# ======================================================================================================================
# zipfile - from the standard library
# ======================================================================================================================
# https://www.geeksforgeeks.org/working-zip-files-python/
# also see bezpy_58_zlib for compressing strings, objects
# ======================================================================================================================
# z = ZipFile(path_to_the_zip_file, mode='r' or mode='w')
# z.printdir() method prints a table of contents for the archive.
# z.extractall() method will extract all the contents of the zip file to the current working directory.
# z.extract() method to extract any file by specifying its path in the zip file.
# z.read(name_of_file_to_read)
# infolist() method creates an instance of ZipInfo class which contains all the information about the zip file.


import os
import datetime
from zipfile import ZipFile, BadZipFile

  
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
  
def zip_all_files(directory, zip_file_name):

    # calling function to get all file paths in the source directory
    file_paths = get_all_file_paths(directory) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(f'\t{file_name}')
  
    # writing files to a destination zipfile and implicitly close the file
    with ZipFile(zip_file_name, 'w') as zip:
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 

    print('All files zipped successfully!')         


def print_zip_info_list(zip_object):
    print(zip_object.infolist())
    for info in zip_object.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')


if __name__ == "__main__":

    directory = '.\\myzip\\source'   # all source files in this directory
    zip_file_name = '.\\myzip\\my_zipped_files.zip'  # final zip file full path

    zip_all_files(directory, zip_file_name)

    zip = ZipFile(zip_file_name, 'r')
    zip.printdir()     # printing all the contents of the newly created zip file. Notice the file paths from root directory are preserved with the zipped file 'myzip/source/...'
#   File Name                                      Modified                       Size
#   myzip/source/a.txt                             2024-08-01 17:02:56            3
#   myzip/source/b.txt                             2024-08-01 17:02:56            3
    # ---- data = zip.read('\\myzip\\source\b.txt')
    zip.close()

    zip_file_name = '.\\myzip\\zipped_c_and_d.zip'
    zip = ZipFile(zip_file_name, 'r')
    zip.printdir()   # Notice these files were zipped in the same directory as the final zip file => there are not paths in the file name
#   File Name                                      Modified                       Size
#   c.txt                                          2024-08-01 17:02:58            3
#   d.txt                                          2024-08-01 17:02:58
    zip.extract(member='c.txt', path='.\\myzip\\dest', pwd=None)   # member is the path within the zip file, and can take a ZipInfo object also
    zip.extractall(members=None, path='.\\myzip\\dest', pwd=None)   # extracting all the files default path is current working directory i.e. os.getcwd()
    zip.close()

    # Handle a bad zipfile
    file_name = r'C:\\github\\myzip\\bad_zip_file.zip'
    try:
        zip = ZipFile(file_name, 'r')
    except BadZipFile:
        print('zip file is bad')

# ======================================================================================================================
# zip.infolist()
# ======================================================================================================================
# file_name = "example.zip" # specifying the zip file name
# with ZipFile(file_name, 'r') as zip:           # opening the zip file in READ mode
#     for info in zip.infolist():
#         print(info.filename)
#         print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
#         print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
#         print('\tZIP version:\t' + str(info.create_version))
#         print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
#         print('\tUncompressed:\t' + str(info.file_size) + ' bytes')