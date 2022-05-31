# quotes email sender

import datetime as dt
import smtplib

# step 1 use the datetime to determine the current day of the week
import random

now = dt.datetime.now()
day_number = now.weekday()
print(day_number)

# step 2 open the the file and obtain the LIST of quotes


with open("quotes.txt") as data_file:
    data = data_file.readlines()

    # step 3 use random module to pick a random quote from the LIST
    quote = random.choice(data)

# step 4 use smtplib to send the email to yourself

my_gmail = "us2313s14@gmail.com"
password = "Abcd1234$"

if day_number == 2:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="rjowvywbb@laste.ml",
            msg=f"Subject:Motivational quote of the day\n\n{quote}"
        )
