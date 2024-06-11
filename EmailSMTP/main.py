import random
import smtplib
from datetime import *

if datetime.weekday == 0:
    with open(file='quotes.txt') as file:
        # file = file.readlines()
        # file = random.choice(file)
        # message = file
        # print(message)

        file = file.read().split('\n')
        index = random.randint(0, len(file))
        message = file[index]

    message = message.split('"')
    # print(message[2])
    # print(message)

    SENDER = 'ranahimanshu335@gmail.com'
    PASSWORD = '1234567890123456' # Add your password here (must be 16 digits)
    RECEIVER = 'kalatomu@gmail.com'

    conn = smtplib.SMTP("smtp.gmail.com")
    conn.starttls()
    conn.login(SENDER, PASSWORD)
    conn.sendmail(from_addr=SENDER,
                  to_addrs=RECEIVER,
                  msg=f'{message[1]}\n{message[2]}')
    conn.close()

else:
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f"Today's {weekday[datetime.now().weekday()]}, you have to wait for Monday.")
