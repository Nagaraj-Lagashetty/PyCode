import shutil
import smtplib   #Simple mail transfer protocol

while True:
    x,y,z = shutil.disk_usage('E:\\')
    Total,Used,Free = (x//2**30),(y//2**30),(z//2**30)
    print('Total - {} GB\nUsed  - {} GB\nFree  - {} GB'.format(Total,Used,Free))
    if Free > 184 :
        def Send_email(sub, msg):
            try:
                connection = smtplib.SMTP('smtp.gmail.com', 587)
                # Gmail - smtp.gmail.com , 587
                # yahoo - smtp.mail.yahoo.com , 587
                # outlook/hotmail - smtp-mail.outlook.com , 587
                connection.ehlo()  # connection to server
                connection.starttls()  # ecryption
                connection.login('*@gmail.com', '*****')
                message = 'Subject: {}\n\n{}'.format(sub, msg)
                To = '*@gmail.com'
                connection.sendmail('*@gmail.com', To.split(','), message)
                connection.quit()
                print('Email sent successfully')

            except:
                print('Email failed')
        subject = 'Disk space alert Mail'
        Message = '''Hi 

                    E:// drive is about full.
                    Kindly perform the clean up.

                    Thank you
                    Nagaraj'''
        Send_email(subject, Message)
        break
print('Out of while loop')