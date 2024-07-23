##############################################################################################################
### aligns the dictionary text so that the ':' is exactly 30 chars from the edge to align it
##############################################################################################################



##############################################################################################################
# BEFORE
##############################################################################################################
#'Chef' :  'Occupation Group 3' ,
#'Civil Service' :  'Occupation Group 4' ,
#'Claims Examiner' :  'Occupation Group 3' ,
#'Cleaning' :  'Occupation Group 5' ,
#'Clerical' :  'Occupation Group 4' ,
#'CNA' :  'Occupation Group 3' ,
##############################################################################################################
# AFTER
##############################################################################################################
#'Chef'                        :  'Occupation Group 3' ,
#'Civil Service'               :  'Occupation Group 4' ,
#'Claims Examiner'             :  'Occupation Group 3' ,
#'Cleaning'                    :  'Occupation Group 5' ,
#'Clerical'                    :  'Occupation Group 4' ,
#'CNA'                         :  'Occupation Group 3' ,
##############################################################################################################






f_in = open('in.txt', 'r')
f_out = open('out.txt', 'w')
lines_list = f_in.readlines()
for line in lines_list:
        x = line.find(':')
        f_out.write(line[0:x] + ' '*(30-x) + line[x:])

f_in.close()
f_out.close()




