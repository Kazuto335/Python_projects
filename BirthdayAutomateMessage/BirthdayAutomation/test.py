# with open(file='birthdays.csv') as birthday_list:
#     print(birthday_list.read())

from pandas import *
df = read_csv('birthdays.csv')
# print(df.shape[0])
# print(len(df.index))

# MONTH = 0
# DAY = 0
for index in range(0, len(df.index)):
    MONTH = df.at[index, 'month']
    DAY = df.at[index, 'day']
    NAME = df.at[index, 'name']

print(f"{DAY}/{MONTH}")

from random import *
from datetime import *

list_of_files = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

current_day = datetime.now().day
current_month = datetime.now().month

if current_day == 11 or current_month == 6:
    OLD_NAME = '[NAME]'
    NEW_NAME = NAME
    letter_template = choice(list_of_files)
    with open(file=f'letter_templates/{letter_template}') as letter:
        letter = letter.read()
        LETTER = letter.replace(OLD_NAME, NEW_NAME)

# print(LETTER)

import smtplib

SENDER = 'ranahimanshu335@gmail.com'
PASSOWRD = '1234567890123456' # your password here.
RECEIVER = 'kalatomu@gmail.com'

with smtplib.SMTP('smtp.gmail.com') as conn:
    conn.starttls()
    conn.login(SENDER,PASSOWRD)
    conn.sendmail(SENDER,RECEIVER,msg=LETTER)
    conn.close()








