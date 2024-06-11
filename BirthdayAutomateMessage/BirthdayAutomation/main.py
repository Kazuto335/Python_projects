from tkinter import messagebox
from pandas import *
from datetime import *
from random import *
from smtplib import *

SENDER = 'ranahimanshu335@gmail.com'
PASSOWRD = '1234567890123456' # your password here.
LIST_OF_LETTERS = ('letter_1.txt', 'letter_2.txt', 'letter_3.txt')

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
df = read_csv('birthdays.csv')
# print(df.shape[0])
# print(len(df.index))
for index in range(0, len(df.index)):
    receiver = df.at[index, 'email']
    # print(type(RECEIVER))
    MONTH: object = df.at[index, 'month']
    DAY: object = df.at[index, 'day']
    NAME = df.at[index, 'name']

    # print(f"{DAY}/{MONTH}")
    # 2. Check if today matches a birthday in the birthdays.csv
    current_day = datetime.now().day
    current_month = datetime.now().month

    if current_day == DAY and current_month == MONTH:

        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv
        letter_template = choice(LIST_OF_LETTERS)
        OLD_NAME = '[NAME]'
        NEW_NAME = NAME
        with open(file=f'letter_templates/{letter_template}') as letter:
            letter = letter.read()
            LETTER = letter.replace(OLD_NAME, NEW_NAME)

        # 4. Send the letter generated in step 3 to that person's email address.
        with SMTP('smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(SENDER, PASSWORD)
            conn.sendmail(SENDER, receiver, msg=LETTER)
            conn.close()
            messagebox.showinfo('Done', f'Message Send to {NEW_NAME}')
    else:
        messagebox.showinfo("Nobody's BIRTHDAY", "Nobody's birthday today.")
