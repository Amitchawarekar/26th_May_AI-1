import smtplib
import imaplib
import email
import credentials as cr
from bs4 import BeautifulSoup

mailer = imaplib.IMAP4_SSL('smtp.gmail.com')
mailer.login('amit.chawarekar@gmail.com','yxpovifozajrehpp')
mailer.select('inbox')

t, data = mailer.search(None,'ALL')

email_ind = data[0]

indx = email_ind.split()
latest_mail_ind = indx[-1]
first_mail_ind = indx[0]

t1,data_mail = mailer.fetch(latest_mail_ind, '(RFC822)')
data1 = data_mail[0]
for i in data1:
     soup=BeautifulSoup(text,'html.parser')
     h2=[i.text for i in soup.find_all('h2')]
     print(h2)
     #print(i.decode())
