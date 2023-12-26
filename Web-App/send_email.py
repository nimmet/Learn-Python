import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = ""
password = ""

receiver = "hello@example.com"
context = ssl.create_default_context()

message = """\
Subject: Hi
Hallo!
Wie geht es dir?
Tschuss!

"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username, receiver, message)


