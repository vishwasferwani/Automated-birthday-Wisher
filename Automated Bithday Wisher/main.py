
import random
import pandas
import datetime as dt
import smtplib

my_email= "try1234vishwas@gmail.com"
password = "nqyn qeuc ciiw dnss"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month,today_day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"] , data_row["day"]):data_row for (index,data_row) in data.iterrows()}

letter_no = random.randint(1,3)
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"letter_templates/letter_{letter_no}.txt") as letter:
        msg = letter.read()
        new_msg= msg.replace("[NAME]",birthday_person["name"])
    reciever = birthday_person["email"]
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=reciever ,msg=f"Subject:HAPPY BIRTHDAY\n\n{new_msg}")


