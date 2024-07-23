
import csv

# ======================================================================================================================
# csv.writer Converts list of Tuples to CSV format
# ======================================================================================================================
data = [('COLA', 'COLB', 'COLC'),
         (1, 2, 3),
         (4, 5, 6),
         (7, 8, 9),
         (10,11,12)]
columns = len(data[0])
rows = len(data)

f1 = open('myfiles\op1.csv', 'w')
f2 = open('myfiles\op2.csv', 'w')

writer1 = csv.writer(f1)  # This duplicates the next-line char
writer2 = csv.writer(f2, lineterminator='\n')  # Need lineterminator else will duplicate the next-line char
for row in range(rows):
    writer1.writerow(data[row])
    writer2.writerow(data[row])

f1.close()
f2.close()



# ===============
#  op1.csv ...
# ===============
# COLA,COLB,COLC
#
# 1,2,3
#
# 4,5,6
#
# 7,8,9
#
# 10,11,12


# ===============
#  op2.csv ...
# ===============
#  COLA,COLB,COLC
#  1,2,3
#  4,5,6
#  7,8,9
# 10,11,12



# Notice entry 'string,three' has a comma
data = [('COLA','COLB','COLC'),('string1','string2','string,three'),(4,5,6),(7,8,9)]
rows = len(data)
with open(r'myfiles\op3.csv', 'w') as test_file:
  writer3 = csv.writer(test_file, lineterminator='\n') #need lineterminator else will duplicate the next-line char
  for row in range(rows):
    writer3.writerow(data[row])

# ===============
#  op3.csv ...
# ===============
#  COLA,COLB,COLC
#  string1,string2,"string,three"
#  4,5,6
#  7,8,9



# ======================================================================================================================
# csv.reader - You can use the next() function or simply loop thru the reader
# ======================================================================================================================
# Note easier to read csv file into dataframe  pd.read_csv()
with open('myfiles\op2.csv', 'r') as f:
    reader = csv.reader(f)   # This is an iterator and is iterable
    header_row = next(reader)  # Returns list
    print(header_row)
    for row in reader:
        print(row)            # each row is a list

# ['COLA', 'COLB', 'COLC']
# ['1', '2', '3']
# ['4', '5', '6']
# ['7', '8', '9']
# ['10', '11', '12']

