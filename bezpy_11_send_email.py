# ======================================================================================================================
# Program: send_email.py  see http://naelshiab.com/tutorial-send-email-python/ for basic example
# Function: Sends email with bodytext, attachments can be listed, or an entire directory

# Sample Use:
#   send(['obezalely@tscinsurance.com'], "Subject goes here", "html body here", r'C:\T2\five.txt', r'C:\T2\Directory')
# Sample Use from Command Prompt:
#>>> python send_email.py  obezalely@tscinsurance.com  "SUBJECT GOES HERE" "MESSAGE GOES HERE" C:\ValidPath\report1.txt C:\ValidPath\report2.txt
#>>> python send_email.py  obezalely@tscinsurance.com  "SUBJECT GOES HERE" "MESSAGE GOES HERE"           # NO ATTATCHMENTS
#>>> python send_email.py  obezalely@tscinsurance.com  "SUBJECT GOES HERE" "" C:\ValidPath\report1.txt   # NO BODY MESSAGE
#>>> python send_email.py  obezalely@tscinsurance.com  "SUBJECT GOES HERE"                               # SUBJECT ONLY


# ARG1 = <tscinsurance email address list of recipients>
# ARG2 = <subject of the email as string>
# ARG3 = <body text in html> optional
# ARG4 .... ARGN = list of files or directories separated by spaces,
#            note: the directories will be browsed for any file content

# Notes:  for 'server.sendmail(FROMADDR, toaddr_list, text)',  toaddr_list is a list of email addresses
# e.g.  ['oren.bezalely@gmail.com','obezalely@tscinsurance.com'].  The email will be sent to that list.  Whatever
# emails are listed in msg['To'] or msg['Cc'] will be displayed on the header.  So any email which appears in
# toaddr_list but not in msg['To'] or msg['Cc'] will be blind. There is no field msg['Bcc']

# MIMEText: It consists of simple text. This will be the body of the email.
# MIMEImage: This would allow us to add images to our emails.
# MIMEAudio: If we wish to add audio files, we may do it easily with the help of this subclass.
# MIMEApplication: This can be used to add anything or any other attachments.

import sys
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
#from email.mime.image import MIMEImage  # For attaching images
from email import encoders
from email.utils import formataddr
from time import sleep


# HEADER_NAME = 'ONB REPORTS'
# FROMADDR = "Oren Bez"
# USER = "oren.bezalely@gmail.com"
# PSSWD = "opwp jcqo nbdd zzvc"    # < -- created new app password 'bezpy_email' on  9/9/2024 here: https://myaccount.google.com/apppasswords
# SMTP = 'smtp.gmail.com'
# PORT = 587


# HEADER_NAME = 'ONB REPORTS'
# FROMADDR = "oren@bezalely.net"
# USER = "oren@bezalely.net"
# PSSWD = "Bez7383Ore"
# SMTP = 'mail.bezalely.net'
# PORT = 587


# HEADER_NAME = 'ONB REPORTS'
# FROMADDR = "oren.bezalely@outlook.com"
# USER = "oren.bezalely@outlook.com"
# PSSWD = "badge7383"
# SMTP = 'smtp.office365.com'
# PORT = 587


# see EastCoastUSA google sheets, Software tab
HEADER_NAME = 'ONB REPORTS'
FROMADDR = "orders@ecusad.com"
USER = "7cc91c001@smtp-brevo.com"
PSSWD = "brDzwsnFVSEZ9243"
SMTP = 'smtp-relay.brevo.com'
PORT = 587


# ======================================================================================================================
#   validate_args():
# ======================================================================================================================
def validate_args():
    sample = "Usage: send(<recipient-email-list>, <subject>, <html-body>, <path1orfile1>, <path2orfile2>, ... "
    if len(sys.argv) == 1:
        print("Error 1: No email address passed.\n" + sample)
        sys.exit(1)
    elif len(sys.argv) == 2:
        print("Error 2: No subject passed.\n" + sample)
        sys.exit(2)

        
# ======================================================================================================================
#   validate_email(email_addr):
# ======================================================================================================================
def validate_email(email_addr):
    exception_set = {'jeff@interactivelimited.com',
                     'dave@interactivelimited.com',
                     'oren@bezalely.net',
                     'oren.bezalely@gmail.com',
                     'bezoren@gmail.com',
                     'julian@fhia.net',                   # Julian Labossiere
                     'js@business-sci.com',               # Josh speyer
                     }
    match = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_addr)
    if not match:
        print(f'Email address: {email_addr} appears to be invalid')
        return False

    if (email_addr in exception_set) or email_addr.endswith('@tscinsurance.com') or email_addr.endswith('@stillwater.com'):
        return True
    else:
        print(f'Email address: {email_addr} is not a valid recipient')
        return False


# ======================================================================================================================
#   add_file (fp): input file path as string e.g. 'C:\temp\file.txt'
# ======================================================================================================================
def add_file (fp): 
    file_list.append((fp,os.path.basename(fp)))


# ======================================================================================================================
#   generate_file_list(fl):
# ======================================================================================================================
def generate_file_list(fl):
    #e.g. fl = (r'C:\T2\five.txt', r'C:\T2\store', r'C:\T2\six.txt', r'C:\T2\four.txt')
    # loops through all paths/files in arguments and checks if valid
    for i in fl:
        if os.path.isfile(i) == True:
            add_file(i)
        elif  os.path.isdir(i) == True:
            for subdir, dirs, files in os.walk(i):
                for file in files:
                    add_file(os.path.join(subdir, file))
        else:
            print("Error 3: \'"+ i + "\' is an invalid path!!!")
            sys.exit(3)

# ======================================================================================================================
#   send(toaddr, subject, bodytext='', *fl):
# ======================================================================================================================
def send(toaddr_list, subject, bodytext='', *fl):
    """ Sends email to recipient list  <toaddr_list>  with <subject> and <bodytext>, you can add an optional number of
        files and file directories as comma separated arguments *fl  e.g.  'myfile.txt', r'C:\mypath\dir\' this will
        attach all files in the selected directory.  Relative or absolute paths may be used for the attachments."""

    # For backward compatibility - may have passed a string of one email instead of list of emails
    if type(toaddr_list) == str:
        toaddr_list = [toaddr_list]

    msg = MIMEMultipart()

    ##   THIS SECTION IS JUST FOR DISPLAY FOR THE EMAIL HEADER
    #msg['From'] = 'TSC REPORTS'
    #msg['From'] = formataddr(('TSC REPORTS', FROMADDR))  # default charset='utf-8'
    msg['From'] = formataddr((str(Header(HEADER_NAME, 'utf-8')), FROMADDR))
    msg['Subject'] = subject        # e.g.  "Tina's Report Files Enclosed"
    #msg['To'] = 'undisclosed-recipients'  # This APPENDS to the recipient list, it does not SET it.
    #msg['Cc'] = 'addr@email.com'

    global file_list
    file_list = []

    body = f'{bodytext}<br><br>'

    if fl:  #if there are files to attach.
        generate_file_list(fl)
        body += '<span style="color:DarkRed;font-face=monspace;white-space:pre;font-weight:bold">Reports Attached: '
        for fp,fn in file_list: # (filepath, filename)
            if fn.endswith('.db') == False: #exclude 'Thumbs.db'
                body += f'{fn}  '
                attachment = open(fp,"rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename=" + fn)
                msg.attach(part)
        body += '</span><br>'


    body += "<br><img src='https://bezalely.net/images/Suzuki5.jpg' alt='suzuki' width='180'><br><br>"


    msg.attach(MIMEText(body, 'html'))   #USE FOR HTML EMAILS
    #msg.attach(MIMEText(body, 'text'))  #USE FOR TEXT EMAILS

    try:
        server = smtplib.SMTP(SMTP, PORT)
    except:
        message_5 = f"Error 5: unable to set up server smtplib.SMTP({SMTP}, {PORT})"
        print (message_5)
        return message_5

    try:
        # server.set_debuglevel(1)  # Sets Debugger Which Prints Full Communication output
        
        # Identify the domain name of the sending host to SMTP
        server.ehlo()    # EHLO is an alternative to HELO for servers that support the SMTP service extensions (ESMTP)
        # server.helo()  # if the above fails use .helo()

        server.starttls()
        server.login(USER, PSSWD)

    except:
        message_6 = f"Error 5: unable to login to SMTP server server.login({USER}, {PSSWD})"
        print(message_6)
        server.quit()
        return message_6

    for recipient in toaddr_list:
        if validate_email(recipient)== False:
            message_7 = f"Error 7: {recipient} is an invalid recipient email address!!!"
            print(message_7)
            server.quit()
            return message_7
    text = msg.as_string()
    try:
        response = server.sendmail(FROMADDR, toaddr_list, text)
        print(f"server.sendmail({FROMADDR=}, {toaddr_list=})")
        sleep(1)
    except Exception as e:
        message_8 = f"Error 8: Unable to send email to {toaddr_list}"
        print(message_8, e)
        server.quit()
        return message_8

    server.quit()
    message_9 = f"Success: Emails have been sent to {toaddr_list}"
    print(message_9)

    return message_9


# ======================================================================================================================
#  __name__ == "__main__":  FOR TESTING ONLY
# ======================================================================================================================
if __name__ == "__main__":

    # sample input fields to command line for regression testing
    #sys.argv = ['send_email.py']
    #sys.argv = ['send_email.py', 'oren@bezalely.net', 'SUBJECT']
    sys.argv = ['send_email.py', 'bezoren@gmail.com', "TEST 345"]
    #sys.argv = ['send_email.py', 'obezalely@tscinsurance.com', 'TEST 8934', 'Regards,<br>Goodbye!']
    #sys.argv = ['send_email.py', ['oren.bezalely@gmail.com','obezalely@tscinsurance.com'], 'TEST 99999', 'Regards,<br>Goodbye!', 'test.txt']
    #sys.argv = ['send_email.py', ['obezalely@tscinsurance.com'], 'Subject goes here', 'body text here', 'test.txt']
    #sys.argv = ['send_email.py', ['oren.bezalely@gmail.com', 'obezalely@tscinsurance.com'], 'Subject goes here', '', r'C:\OrenDocs\Projects\TSC-299 HO Brokers\Notes.txt']


    validate_args()
    t = tuple(sys.argv[1:])    
    send(*t)
    # sys.exit(0)


# ======================================================================================================================
# Also from the standard library ....
# poplib: This module provides a POP3 client interface.
# imaplib: This module provides an IMAP client interface.
# imghdr: This module identifies the type of image file from the contents of the file.
# mailbox: This module provides an interface to Unix mailboxes.
# mimetypes: This module provides a mapping of MIME types to file extensions.
# ssl: This module provides support for Secure Sockets Layer (SSL) connections.
# ======================================================================================================================