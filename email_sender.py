  
import smtplib
import credentials as cr

rx = 'amit4.chawarekar@gmail.com'
sub = 'Another Topic'
msg = 'It has come from python again'

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(cr.auth['user_name'],cr.auth['password'])

email_body = '\r\n'.join(['To:%s'%rx, 'From:%s'%(cr.auth['user_name']),
                          'Subject:%s'%sub, '',msg])

mailer.sendmail(cr.auth['user_name'],rx,email_body)
print('Email sent')
