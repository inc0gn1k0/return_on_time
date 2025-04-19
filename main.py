# Entry point for your project

#start with coding the core inputs required

import numpy as np
import pandas as pd
import datetime as dateime
import logic.utils as utils
from web import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

'''
#This is how the application logic started, before we separated it out into base.py, behaviour.js and form.html
gender = str(input("What is your gender? "))

age_of_ancestor_1_on_your_mothers_side = int(input(f"What was the age of the closest direct {gender} ancestor on your mothers side when they died?"))
age_of_ancestor_2_on_your_mothers_side = int(input(f"What was the age of the second closest direct {gender} ancestor on your mothers side when they died?"))
age_of_ancestor_1_on_your_fathers_side = int(input(f"What was the age of the closest direct {gender} ancestor on your fathers side when they died?"))
age_of_ancestor_2_on_your_fathers_side = int(input(f"What was the age of the second closest direct {gender} ancestor on your fathers side when they died?"))

while True:
    user_input = input("When were you born? (dd-mm-yyyy):")
    try:
        date = dateime.datetime.strptime(user_input, '%d-%m-%Y').date()
        break
    except ValueError:
        print("Invalid date format. Please enter the date in the format dd-mm-yyyy.")

age_in_days = utils.determine_age_in_days_of_user(date)

ancestor_1_mum = age_of_ancestor_1_on_your_mothers_side
ancestor_2_mum = age_of_ancestor_2_on_your_mothers_side
ancestor_1_dad = age_of_ancestor_1_on_your_fathers_side
ancestor_2_dad = age_of_ancestor_2_on_your_fathers_side

your_likely_max_age = utils.avg_max_age(ancestor_1_mum, ancestor_2_mum, ancestor_1_dad, ancestor_2_dad)

time_left = utils.how_long_do_you_have(your_likely_max_age, age_in_days)

print(f"Your likely maximum age is {your_likely_max_age} days")
print(f"Your {age_in_days} days old")

print(f"\nYou have {time_left} days left (likely)")

expiry_date = utils.expiry_date(time_left)

print(f"Your expiry date is {expiry_date}.")

'''



#Now compute how much time is available in years, months, days, hours, minutes and seconds...by launching a counter in YYYY-MM-DD HH:MM:SS
#this is after taking into account the average max age of the ancestors less your current age
#this launches the counter






#We now go deeper into how much time you have. Since the average human spends 8 hours a day asleep, x amount eating, y defacating, z grooming...we arrive at your available wakeful hours of w 







#We then want to use a GPT openAI call that prompts GPT: Do I have time for {this_shit} given {w} available to me? Give me a response in short if I do have time for it, but if I do not have time for it, tell me how I'll have committed roughly t/w*100 of my wakeful lifespan on {this shit}.






#then we dress everything up into a simple django web app, launch on our own domain: return_on_time.com











