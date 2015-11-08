import  smtplib

smtpUser = ''
smtpPass = ''

toAdd = ''
fromAdd = smtpUser

subject = ''
header = 'To: ' + '\n' + 'From: ' + fromAdd + '\n' + 'Subject :' +  subject
body = ''

print header + '\n' + body

smtp = smtplib.SMTP('smtp.gmail.com', 587)

smtp.ehlo()
smtp.starttls()
smtp.ehlo()

smtp.login(smtpUser, smtpPass)
smtp.sendmail(fromAdd, toAdd, header + '\n\n' + body)

smtp.quit()