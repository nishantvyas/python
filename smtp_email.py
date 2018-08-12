"""
go to https://www.google.com/settings/security/lesssecureapps and "Allow less secure apps".

Create an SMTP object for connection to the server.
Log in to your account.
Define your message headers and login credentials.
Create a MIMEMultipart message object and attach the relevant headers to it, i.e. From, To, and Subject.
Attach the message to the message MIMEMultipart object.
Finally, send the message.

"""


from email.message import EmailMessage
import smtplib


# create message object instance
msg = EmailMessage()

# create message object instance
message = """
<html>
<body>

<h1>My First Heading</h1>

<table id="t01">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>Nishant</td>
        <td>Vyas</td>
        <td>35</td>
      </tr>
    </table>

</body>
</html>

"""

# setup the parameters of the message
password = ""
msg['From'] = "knullreport@gmail.com"
msg['To'] = "nishantvyas@gmail.com"
msg['Subject'] = "Knull Test Report"

# add in the message body
msg.add_header('Content-Type', 'text/html')
msg.set_payload(message)

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
#start tls session
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))