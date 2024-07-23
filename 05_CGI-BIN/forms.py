#!/usr/bin/python
"""
https://darksky.net/dev/account
User: oren.bezalely@gmail.com
Pwd:  badge7383 or 

"""

import sys  # print(sys.version_info[:]) prints full version of python
import cgi  # used for retrieving POST/GET
#import cgbit #displays error messages
#cgbit.enable()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>FORM PRACTICE</title>')
print ('</head>')
print ('<body>')
print ('<h2>FORM PRACTICE</h2>')


form=cgi.FieldStorage()
if form.getvalue("name"): # is not empty
	print ('<hi> hello ' + form.getvalue("name"))
if form.getvalue("happy"): # is not empty
	print ('<p>Glad you are happy</p>')
if form.getvalue("sad"): # is not empty
	print ('<p> sorry to hear that </p>')


print ('<form method="post" action="" >')
print ('Name: <input type="text" name="name" >')
print ('<input type="checkbox" name="happy" >Happy')
print ('<input type="checkbox" name="sad" >Sad<br><br>')
print ('<input type="submit"	value ="SUBMIT">')
print ('</form>')

#print '<p>cgi.FieldStorage()=' + str(form) + '<br></p>'


print ('</body>')
print ('</html>')