import smtplib, ConfigParser, SNMT

config = ConfigParser.ConfigParser()
config.read('config.ini')

# Sender Info
SENDER = config.get('Sender', 'email')
PASSWORD = config.get('Sender', 'password')

# Receiver Info
TO = config.get('Receiver', 'to')
SUBJECT = config.get('Receiver', 'subject')
TEXT = config.get('Receiver', 'text')

# Carrier Info
SERVER = config.get('Carrier', 'server')
PORT = config.getint('Carrier', 'port')

if not SNMT.TEXT:
    # Create connection to carrier service
    server = smtplib.SMTP(SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(SENDER, PASSWORD)

    BODY = '\r\n'.join([
        'To: %s' % TO,
        'From: %s' % SENDER,
        'Subject: %s' % SUBJECT,
        '',
        SNMT.TEXT
        #TEXT
        ])

    try:
        server.sendmail(SENDER, [TO], BODY)
        print 'email sent'
    except:
        print 'error sending email'

    server.quit()
else:
    exit()
