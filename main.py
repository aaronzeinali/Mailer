import smtplib
from time import sleep
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print('\n** Welcome to BooMail **\nFill in the blanks to continue...')

def main():
    ### informations
    print('* Server informations *')
    smtp = input('Enter the smtp url:(example: smtp.gmail.com) ')
    port = int(input('Enter the port number: '))
    print('* Account informations *')
    account = input('Enter the account: ')
    password = input('Enter the password: ')
    print('* Receiver informations *')
    receiver = input('Enter the receiver: ')
    subject = input('Enter the subject: ')
    txt = input('Enter the path of text file: ')
    ### connection
    server = smtplib.SMTP(smtp, port)
    server.ehlo()
    server.login(account, password)
    ### message
    message = MIMEMultipart()
    message['from'] = account
    message['to'] = receiver
    message['subject'] = subject
    with open(txt, 'r') as n:
        msg = n.read()
    message.attach(MIMEText(msg, 'plain'))
    text = message.as_string()

    ### sending message
    def sendingmail():
        try:
            success = server.sendmail(account, receiver, text)
            print('\n[*] Email sent successfully\n')
        except:
            tryagain = input('Something went wrong! Try again? Y/n\n')
            if tryagain == 'y' or 'Y':
                sendingmail()
            elif tryagain == 'N' or 'n':
                quit()
            else:
                print('Command not found!')
                quit()

    sendingmail()


main()


def ending():
    cont = input('Do you want to continue? Y/n\n')
    if cont == 'y':
        print('\n')
        main()
        ending()
    elif cont == 'Y':
        print('\n')
        main()
    elif cont == 'n' or 'N':
        print('\nThanks for using BooMail!\nHave a good time\n')
        sleep(5)
        quit()
    else:
        print('Command not found')


ending()
