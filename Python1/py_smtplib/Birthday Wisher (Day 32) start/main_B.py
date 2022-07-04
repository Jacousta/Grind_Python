import smtplib
import random
import datetime as dt

time = dt.datetime.now()
date = time.date()
month = time.month
day_of_week = time.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        my_email = "cpunia_be21@thapar.edu"

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password="vkvxepmlfrepdiin")
        connection.sendmail(from_addr=my_email, to_addrs="chiragpunia750@yahoo.com",
                            msg=f"SUBJECT:{random.randint(1,100)} \n\n {quotes_list[random.randint(1, 101)]}")
        connection.quit()
