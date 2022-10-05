# import smtplib

# my_email = "sereil@live.ca"
# password = None
# with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:

#     '''Secure the Connection using TLS'''
#     connection.starttls()

#     '''Set Credentials'''
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="helixwtf@gmail.com",msg ="Subject:Testing!\n\nThis is the body of my email")

import datetime as dt

#now = dt.datetime(year=2022,month=10,day=5)
now = dt.datetime.now()
year = now.year
month= now.month
day_of_week = now.weekday() #From 0 to 6 where 6 is Sunday


print(now)

