import requests
from datetime import datetime, timezone, timedelta
import smtplib, config

MY_LAT = 37.593516 # Your latitude
MY_LONG = 126.673763 # Your longitude

my_latlong = (MY_LAT, MY_LONG)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

current_latlong = (iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.
def is_above_head(current:tuple[float, float]):
    return abs(current[0] - MY_LAT) <= 5 and abs(current[1] - MY_LONG) <= 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid" : "Asia/Seoul"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# timezone, timedelta import
# +9 이라는 타임존 객체 생성
# 해당 타임존 객체를 기준으로 datetime.now() 실행
KST = timezone(timedelta(hours=9))
time_now = datetime.now(KST)
now_hour = time_now.hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_above_head(current_latlong):
    if sunset < now_hour or now_hour < sunrise:
        from email.message import EmailMessage

        message = EmailMessage()
        message['Subject'] = "머리 위를 보세요"
        message['From'] = config.SMTP_CONFIG["user"]
        message['To'] = config.SMTP_CONFIG["user"]
        message.set_content(config.content_mail)

        with smtplib.SMTP(config.SMTP_CONFIG["smtp"]) as connection:
            connection.starttls()
            connection.login(user=config.SMTP_CONFIG["user"], password=config.SMTP_CONFIG["app_pw"])
            connection.send_message(message)

