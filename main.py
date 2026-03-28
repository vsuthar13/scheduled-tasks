##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import smtplib

import pandas as pd
from pathlib import Path
import random
import smtplib as smtp

current_email='XX'
current_password='XX'




now = dt.datetime.now()
current_day = now.day
current_month = now.month
data=pd.read_csv('birthdays.csv')
dir_path = Path('./letter_templates')
files = dir_path.glob('*.txt')
random_file = random.choice(list(files))



for index, row in data.iterrows():
    if row['day'] == current_day and row['month'] == current_month:
        person_name = row['name']
        with open(random_file) as f:
            content = f.read().replace('[NAME]', person_name)

        with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=current_email, password=current_password)
            connection.sendmail(current_email, 'XX@gmail.com',msg=f'Subject: Hello {person_name}!\n\n{content}')




