from flask import Blueprint, render_template, request
from logic.utils import determine_age_in_days_of_user, avg_max_age, how_long_do_you_have, expiry_date
from datetime import datetime

base_bp = Blueprint('base_bp', __name__)

@base_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birth_date = request.form.get('birth_date')
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        gender = request.form.get('gender') 
        ancestors = [
            int(request.form.get('ancestor_1_mum')),
            int(request.form.get('ancestor_2_mum')),
            int(request.form.get('ancestor_1_dad')),
            int(request.form.get('ancestor_2_dad'))
        ]

        age_in_days = determine_age_in_days_of_user(birth_date)
        max_age = avg_max_age(*ancestors)
        time_left = how_long_do_you_have(max_age, age_in_days)
        target_date = expiry_date(time_left)
        return render_template('countdown.html', target_date=target_date)

    return render_template('form.html')