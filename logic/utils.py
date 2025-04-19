import numpy as np
import pandas as pd
import datetime as dateime


def determine_age_in_days_of_user(user_input):
    today = dateime.date.today()
    age_in_days = (today - user_input).days
    return age_in_days



def avg_max_age(ancestor_1_mum, ancestor_2_mum, ancestor_1_dad, ancestor_2_dad): #could also rewrite this to accept a list def avg_max_age(ancestors):
    max_age = np.mean([ancestor_1_mum, ancestor_2_mum, ancestor_1_dad, ancestor_2_dad])*365 #average max age of ancestors in days
    return max_age


def how_long_do_you_have(avg_max_age, age_in_days):
    time_left = avg_max_age - age_in_days
    return time_left


def expiry_date(time_left):
    today = dateime.date.today()
    expiry_date = today + dateime.timedelta(days=time_left)
    return expiry_date.isoformat()

