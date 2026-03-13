##################### Extra Hard Starting Project ######################
import pandas, random
import datetime as dt
import smtplib

LETTER_TEMPLATES = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt","./letter_templates/letter_3.txt"]
MY_MAIL= "test@test.com"
MY_PW = "xxxx xxxx xxxx xxxx"

def send_email(email:str, msg:str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL,password=MY_PW)
        connection.sendmail(from_addr=MY_MAIL,to_addrs=email,msg=msg)


# 1. Update the birthdays.csv
birth_data = pandas.read_csv("./birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
target_month = today.month
target_day = today.day
today_result:pandas.DataFrame = birth_data.loc[(birth_data['month'] == target_month) & (birth_data['day'] == target_day)]
print(today_result)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(today_result) != 0:
    for (index,row) in today_result.iterrows():
        target_name = row["name"]
        target_email = row.email

        with open(random.choice(LETTER_TEMPLATES), mode="r") as template:
            content = template.readlines().copy()
            content[0] = content[0].replace("[NAME]",target_name)
            messages = "".join(content)

            send_email(target_email,messages)


# 4. Send the letter generated in step 3 to that person's email address.




