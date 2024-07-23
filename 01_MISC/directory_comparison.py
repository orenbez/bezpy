import os,sys

def create_set(src):
    file_set = set()
    depth = 0
    for root, dirs, files in os.walk(src):
        # tab = '->' * depth
        # print(f'ROOT:', root)
        # print(f'DIRS:{tab}' + str(dirs))
        # print(f'FILE:{tab}' + str(files))
        for file in files:
            if 'RECYCLER' in root or 'System Volume Information' in root or 'Thumbs.db' in root:
                continue
            x = os.path.join(root, file)
            y = os.path.getsize(x)
            z = os.path.getmtime(x)
            file_set.add((x[len(src):], y, z))
        # depth += 1
        # if depth == 1:
        #     break
    return file_set

src = r'\\TSC1-IMAGE2\images'
dest = r'\\tsc-ny1-nas01\Shares\Imageright3X\Images'

# x = []
# for i in os.listdir(src):    # loops through all files/directories in directory
#     if os.path.isdir(src + '\\' + i):
#         x.append(i)


x = ['12_ACCT', '12_CLMR', '12_CLMS', '12_HQUO', '12_LEG', '12_MISC', '12_QUOT', '12_TEST', '12_UNDR', '12_WWW', 'AUDIT', 'BACKUP', 'castelle', 'Exports', 'filemant', 'Forms', 'FOTOS', 'idxpcl', 'inprint', 'IN_FAXE', 'IN_FAXES', 'IN_FILES', 'locks', 'LOGS', 'Mekel', 'MEMOS', 'MEMOSOUT', 'oasis', 'Outfaxes', 'Outfaxesold', 'OUTPRINT', 'OVERLAYS', 'printbat', 'RightFax', 'Scanner', 'tsc1-image2', 'WFCHART']



z = '12_CLMS'



a = create_set(src + '\\' + z)
b = create_set(dest + '\\' + z)
