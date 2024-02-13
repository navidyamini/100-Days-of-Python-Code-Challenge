import smtplib
import datetime as dt
import random

my_email = "fake_email@fake.com"
password = "fake_password"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.fake.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="second_fake_email@fake.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
# print(year)
# date_of_birth = dt.datetime(year=1900, month=12, day=23)
# print(date_of_birth)
