import datetime as dt
import smtplib

MY_LAT = 31.3256
MY_LNG = 75.5792

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def ist_converter(utc_hour, utc_min):
    if utc_min >= 60:
        temp1 = utc_min / 60
        utc_hour = utc_hour + temp1
        if utc_hour >= 24:
            utc_hour = utc_hour - 24
    return int(utc_hour)


def night_checker(ist_hour_set, ist_min_set,ist_hour, ist_min):
    time_now = dt.datetime.now()
    hour = time_now.hour
    if ist_converter(ist_hour_set, ist_min_set) <= hour <= ist_converter(ist_hour, ist_min):
        return True


def iss_near(response_iss):
    if MY_LAT - 5 <= float(response_iss.json()["iss_position"]["latitude"]) <= MY_LAT + 5 and MY_LNG - 5 <= \
            float(response_iss.json()["iss_position"]["latitude"]) <= MY_LNG + 5:
        return True


def send_email():
    my_email = "cpunia_be21@thapar.edu"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password="vkvxepmlfrepdiin")
    connection.sendmail(from_addr=my_email, to_addrs="chiragpunia750@yahoo.com",
                        msg=f"SUBJECT:ISS_OVERHEAD \n\n LOOK UP IN THE SKY")
    connection.quit()

