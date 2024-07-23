# The program is going to receive a folder or a list of folders to scan, 
# then is going to traverse the directories given and find any duplicated files in the combined set of folders.
# This program is going to compute a hash for every file, allowing us to find duplicated files even though
# their names are different. All of the files that we find are going to be stored in a dictionary,
# with the hash as the key, and the path to the file as the value: { hash: [list of paths] }.



import os, sys
import hashlib

PROGRAM_FILE = os.path.basename(__file__)

def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print(f'Scanning {dirName}...')
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]  # Appends the lists
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print(f'\t\t{subresult}')
            print('___________________')
 
    else:
        print('No duplicate files found.')
 
 
if __name__ == '__main__':
    sys.argv = ['dupes_finder.py', r'.\mydata', r'.\myfiles']
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(i))
            else:
                print(f'{i} is not a valid path, please verify')
                sys.exit()
        printResults(dups)
    else:
        print(f'Usage: python {PROGRAM_FILE} folder or python {PROGRAM_FILE} folder1 folder2 folder3')


# Scanning .\mydata...
# Scanning .\myfiles...
# Scanning .\myfiles\plots...
# Scanning .\myfiles\pyxlwings...
# Duplicates Found:
# The following files are identical. The name could differ, but the content is identical
# ___________________
# 		.\mydata\twitter.json
# 		.\mydata\twitter1.json
# 		.\myfiles\twitter1.json
# ___________________
# 		.\myfiles\IdCard_AP-10109133_1.txt
# 		.\myfiles\IdCard_AP-10109133_2.txt
# 		.\myfiles\touched.txt
# ___________________