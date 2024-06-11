import smtplib

my_email = 'ranahimanshu335@gmail.com'
password = '1234567890123456' # Add your password here (must be 16 digits)
receiver = 'kalatomu@gmail.com'

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs=receiver,
                    msg='Hello\n\nThis is the body of my email.')
connection.close()
#
# from datetime import *
#
# current_time = datetime.now()
# print(current_time)
# year = current_time.year
# month = current_time.month
# day_of_week = current_time.weekday()
# hour = current_time.hour
# minutes = current_time.minute
#
# date_of_birth = datetime(year=2001, month=6, day=25, hour=10)
# print(date_of_birth)
#
#
#
# # print(f'{hour-12}:{minutes}')
# # if year == 2024:
# #     print("Voting Khtm Ho Gai")
