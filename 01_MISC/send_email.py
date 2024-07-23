############################################################################################################
### Program: send_emailer.py  see http://naelshiab.com/tutorial-send-email-python/ for basic example
### Function: Sends email with bodytext, attachements can be listed or an entire directory
### Sample Use: send(obezalely@tscinsurance.com, "Subject goes here", "html body here", r'C:\T2\five.txt', 'C:\T2\Directory')
### ARG1 = <tscinsurance email address of recipient>
### ARG2 = <subject of the email as string>
### ARG3 = <body text in html> optional
### ARG4 .... ARGN = list of files or directories separated by spaces, 
###                  note: the directories will be browsed for any file content
### 07/18/18 - ONB - First Version
### 12/04/18 - ONB - Added exception_set to emailing rules
### 12/06/18 - ONB - Merged with emailer to run as imported module AND from windows command line
### 05/08/19 - ONB - Changed SMTP Settings
############################################################################################################
#!/usr/bin/python3
################################################################################


import sys
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage  # For attaching images
from email import encoders 



################################################################################
### validate_args():
################################################################################
def validate_args():
    sample = "Usage: send(<recipient email>, <subject>, <html-body>, <path1orfile1>, <path2orfile2>, ... "
    if len(sys.argv) == 1:
        print("Error 1: No email address passed.\n" + sample)
        sys.exit(1)
    elif len(sys.argv) == 2:
        print("Error 2: No subject passed.\n" + sample)
        sys.exit(2)

        
################################################################################
### validate_email(email_addr):
################################################################################
def validate_email(email_addr):

    exception_set = {'oren.bezalely@gmail.com',
                     'jeff@interactivelimited.com',
                     'dave@interactivelimited.com'}
    if (email_addr in exception_set):
        return True
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_addr)
    if (match == None) or ('@tscinsurance.com' not in email_addr):
        return False


################################################################################
### add_file (fp): input file path as string e.g. 'C:\temp\file.txt'
################################################################################
def add_file (fp): 
    file_list.append((fp,os.path.basename(fp)))

################################################################################
### generate_file_list(fl):
################################################################################
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

################################################################################
### send(toaddr, subject, bodytext='', *fl):
################################################################################
def send(toaddr, subject, bodytext='', *fl):
    """ Sends email to recipient <toaddr>  with <subject> and <bodytext>, you can add an optional number of
        files and file directories as comma seperated arguments *fl  e.g.  'myfile.txt', 'C:\mypath\dir\' this will attach all 
	files in the selected directory.  Relative or absolute paths may be used for the attachments."""

    if validate_email(toaddr)== False:
        print("Error 4: \'" + toaddr + "\' is an invalid recipient email address!!!")
        sys.exit(4)

 
    msg = MIMEMultipart()
    msg['From'] = 'TSC REPORTS'
    msg['To'] = toaddr       # can use name string here, does not have to be valid email address
    msg['Subject'] = subject # e.g.  "Tina's Report Files Enclosed" 

    global file_list
    
    file_list = []
    
    wordNo = ''
    
    #if there are files to attach.
    if fl:
        generate_file_list(fl)
    else:
        wordNo = ' No '

    body = "<font face='verdana' size='2'><b>" + wordNo + "Reports Attached:</b><br>"

    #Attachments
    for fp,fn in file_list: # (filepath, filename)
        if fn.endswith('.db') == False: #exclude 'Thumbs.db'
            body = body + fn + '<br>'
            attachment = open(fp,"rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename=" + fn)
            msg.attach(part)


    body = body + "<br>" + bodytext + "</font><br><br>"
    body = body + "<img src='https://www.mytscinsurance.com/images/logo.gif' alt='TSC>Direct' width='200'><br><br>"
    body = body + "<font face='verdana' size='1'>"
    body = body + "<i>The contents of this email message and any attachments are intended solely for the addressee(s) and may contain confidential and/or privileged information and may be legally protected from disclosure. If you are not the intended recipient of this message or their agent, or if this message has been addressed to you in error, please immediately alert the sender by reply email and then delete this message and any attachments. If you are not the intended recipient, you are hereby notified that any use, dissemination, copying, or storage of this message or its attachments is strictly prohibited</i>"
    body = body + "</font><br><br>"
    

    msg.attach(MIMEText(body, 'html'))   #USE FOR HTML EMAILS
    #msg.attach(MIMEText(body, 'text'))  #USE FOR TEXT EMAILS

    fromaddr = 'itreports@tscinsurance.com'
    user = "itreports"
    psswd = "7DRqcw%v"
    smtp = 'webmail.tscinsurance.com'
    port = 587


    #fromaddr = "tscmessages@gmail.com"
    #user = "tscmessages@gmail.com"
    #psswd = "prelctxhvypwbgtz"
    #smtp = 'smtp.gmail.com'
    #port = 587


    try:
        server = smtplib.SMTP(smtp, port)
        #server.set_debuglevel(1)  # Sets Debugger Which Prints Full Communication output
        server.starttls()
        server.login(user, psswd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        print ("Error 5: unable to send out email, SMTP Error")
        sys.exit(0)   


    print('Email Has Been Sent To: ' + msg['To'])


################################################################################
###__name__ == "__main__":
################################################################################
if __name__ == "__main__":

    # sample input fields to command line for regression testing
    # sys.argv = ['send_email.py']
    # sys.argv = ['send_email.py', 'oren.bezalely@gmail.com']
    # sys.argv = ['send_email.py', 'oren.bezalely@gmail.com', "Penny's Report Files Enclosed 2"]
    # sys.argv = ['send_email.py', 'obezalely@tscinsurance.com', 'Subject goes here', 'Regards,<br>Goodbye!']
    # sys.argv = ['send_email.py', 'oren.bezalely@gmail.com', 'Subject goes here', 'body text here', r'Dashboard.txt']
    # sys.argv = ['send_email.py', 'oren.bezalely@gmail.com', 'Subject goes here', '', r'C:\OrenDocs\Projects\TSC-299 HO Brokers\Notes.txt']
    # sys.argv = ['send_email.py', 'oren.bezalely@gmail.com', 'Subject goes here', r'C:\OrenDocs\Projects\TSC-299 HO Brokers\Notes.txt']  WARNING - THIS WILL NOT ATTACH FILES

    
    validate_args()
    t = tuple(sys.argv[1:])    
    send(*t)
    sys.exit(0)
