import smtplib, random
import datetime as dt

my_mail= "test@test.com"
my_pw = "xxxx xxxx xxxx xxxx"


# connection = smtplib.SMTP("smtp.test.com")
# connection.starttls()
# connection.login(user=my_mail, password=my_pw)
# connection.sendmail(from_addr=my_mail,to_addrs="test@naver.com",msg="Subject:안녕하세요 메일 보내기 테스트 중이예요\n\n테스트입니다. 이렇게 가능합니다.")
# connection.close()

# """
# Traceback (most recent call last):
#   File "D:\Python\Projects\100dayPython\days\day-32\main.py", line 10, in <module>
#     connection.sendmail(from_addr=my_mail,to_addrs="test@naver.com",msg="Subject:안녕하세요 메일 보내기 테스트 중이예요\n\n테스트입니다. 이렇게 가능합니다.")
#     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\JS\AppData\Local\Programs\Python\Python313\Lib\smtplib.py", line 864, in sendmail
#     msg = _fix_eols(msg).encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 8-12: ordinal not in range(128)
#
# 한글을 넣으면 이렇게 인코딩 오류가 발생하기 때문에
# 별도의 UTF-8 포맷 라이브러리가 필요하다.
# """

from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = "안녕하세요 메일 보내기 테스트 중이예요"
msg['From'] = my_mail
msg['To'] = "test@naver.com"
msg.set_content("테스트입니다. 이렇게 가능합니다.")

# with smtplib.SMTP("smtp.test.com") as connection:
#     # with로 열어서 알아서 close() 해줌
#     connection.starttls()
#     connection.login(user=my_mail, password=my_pw)
#     connection.send_message(msg)

now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(weekday)

# 직접 날짜를 설정해서 datetime 객체를 만들 수도 있음
birthday = dt.datetime(year=2222,month=3,day=13)
print(birthday) # 2222-03-13 00:00:00

with open("quotes.txt") as file:
    quotes_list = file.readlines()

if weekday == 4:
    quote = random.choice(quotes_list)

with smtplib.SMTP("smtp.test.com") as connection:
    connection.starttls()
    connection.login(user=my_mail,password=my_pw)
    msg.set_content(quote)
    connection.send_message(msg)