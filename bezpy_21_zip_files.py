# ======================================================================================================================
# zipfile - from the standard library
# ======================================================================================================================
# https://www.geeksforgeeks.org/working-zip-files-python/
# also see bezpy_58_zlib for compressing strings, objects
# ======================================================================================================================

import os
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
  
def main(): 
    # path to folder which needs to be zipped 
    directory = '.\\myzip\\source'
  
    # calling function to get all file paths in the source directory
    file_paths = get_all_file_paths(directory) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(f'\t{file_name}')
  
    # writing files to a zipfile 
    with ZipFile(directory + '\\..\\my_zipped_files.zip', 'w') as zip:
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 

    print('All files zipped successfully!')         

  
if __name__ == "__main__": 
    main()


    file_name = r'C:\\github\\myzip\\my_zipped_files.zip'
    zip = ZipFile(file_name, 'r')
    zip.printdir()     # printing all the contents of the zip file
    zip.extractall()   # extracting all the files -- not sure where they go
    # zip.extract('python_files/python_wiki.txt')   # method to extract any file by specifying its path in the zip file.
    # data = zip.read(name_of_file_to_read)   # read some specific file
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