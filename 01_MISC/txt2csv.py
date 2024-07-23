############################################################################################################
### Program: txt2csv.py  converts file of encoding 'utf-16-le' = UCS-2 Little Endian BOM (Notepad ++)
###                      to 'utf-8' format for neat opening in .csv format with Excel
### Sample Use: python txt2pdf.py sourcefile.txt outputfile.csv
### 07/31/18 - ONB - First Version, converts data encoding 
### 08/01/18 - ONB - Remove single quotes from the data
############################################################################################################
import codecs
import sys

# Note 'utf-16-le' = UCS-2 Little Endian BOM (Notepad ++)

def txt2utf8(sourceFileName, targetFileName):
    BLOCKSIZE = 1024 # or some other, desired size in bytes
    with codecs.open(sourceFileName, "r", "utf-16-le") as sourceFile:
        with codecs.open(targetFileName, "w", "utf-8") as targetFile:

            #Loop thru the blocks
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                contents = contents.replace(chr(34),'') #Remove all double quotes '"' = chr(34)
                
                if not contents:
                    break
                targetFile.write(contents)



if __name__ == '__main__':

    #sys.argv = ['txt2utf8.py', 'Policy_20180801094728_.txt']  ### FOR TESTING ONLY
    if len(sys.argv) == 2:
        ip_file = sys.argv[1]
        op_file = sys.argv[1].replace('.txt','.csv')
        txt2utf8 (ip_file, op_file )
        print(f"{ip_file} has been successfully converted to {op_file}")
    else:
        print("USAGE: python txt2utf8.py input.txt")
