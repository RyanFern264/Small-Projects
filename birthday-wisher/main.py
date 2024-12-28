import datetime as dt
import os
import random
import pandas as pd
import smtplib

my_email = "testingpython155@gmail.com"
password = ""#removed password since this is getting put in my public git
birthday_person_name = ""
birthday_person_email = ""
birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")
now = dt.datetime.now()
letter_lines = ""

send_email = False
for person in birthdays:
    if person["month"] == now.month and person["day"] == now.day:
        birthday_person_name = person["name"]
        birthday_person_email = person["email"]
        send_email = True

if send_email:
    random_file = random.choice(os.listdir("letter_templates/"))
    with open(f"letter_templates/{random_file}", "r") as file:
        letter_lines = file.readlines()
    letter_lines[0] = letter_lines[0].replace("[NAME]", birthday_person_name)
    letter = ' '.join(str(line) for line in letter_lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ryanfmiami@gmail.com",
                            msg=f"Subject:Happy Birthday!\n\n{letter}")