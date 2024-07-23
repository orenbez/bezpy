import smtplib
from email.message import EmailMessage

# smtplib is the built-in Python SMTP protocol client, to connect to our email account and send mail via SMTP
# MIME (Multipurpose Internet Mail Extensions) is a standard for formatting files to be sent over the internet so they
#       can be viewed in a browser or email application.


FROMADDR = "oren.bezalely@gmail.com"
USER = "oren.bezalely@gmail.com"
PSSWD = "rbdtkcwyqppxadiu"   # Generate App Password with your gmail account
SMTP = 'smtp.gmail.com'
PORT = 587   # Preferred
#PORT = 465   # Only use if 587 is failing


email = EmailMessage() ## Creating a object for EmailMessage
email['from'] = 'Oren Bez'              ## Person who is sending
email['to'] = 'oren.bezalely@stillwater.com'       ## Recipient
# email['to'] = ['recipient1@gmail.com', 'recipient2@gmail.com']   ## Multiple Recipients
email['subject'] = 'Subject Goes Here'  ## Subject of email
# email.set_content("Content Goes Here")  ## Content of email TEXT EXAMPLE

html_content = f"""<!DOCTYPE html>
                    <html>
                        <body>
                            <div style="background-color:#eee;padding:10px 20px;">
                                <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Dear {email['to']}, My newsletter</h2>
                            </div>
                            <div style="padding:20px 0px">
                                <div style="height: 500px;width:400px">
                                    <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                                    <div style="text-align:center;">
                                        <h3>Article 1</h3>
                                        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                                        <a href="#">Read more</a>
                                    </div>
                                </div>
                            </div>
                        </body>
                    </html>"""



email.set_content(html_content, subtype='html')

## Add Attachment
with open(r'.\myfiles\example3.pdf', 'rb') as pdf:
    email.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)


## Sending request to server
with smtplib.SMTP(host=SMTP, port=PORT) as smtp:
    smtp.ehlo()               ## server object
    smtp.starttls()           ## used to send data between server and client
    smtp.login(USER, PSSWD)   ## login id and password of gmail
    smtp.send_message(email)  ## Sending email
    print(f"email sent to {email['to']}")       ## Printing success message