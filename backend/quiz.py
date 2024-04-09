from flask import Blueprint, jsonify, render_template, session, request
from backend.database import  show_users_data, get_test_details, get_test_data, add_users_data
from flask import redirect
from flask import url_for

quiz_bp = Blueprint('quiz', __name__)


@quiz_bp.route('/home')
def index(): #Displays the home page with quiz details.
    # Check if user is logged in
    if 'username' in session:
        data = get_test_details()
        # print(data)
        return render_template('test_section/home.html', data = data, username = session['username'])
    else:
        return redirect(url_for('login.index'))

@quiz_bp.route('/start-quiz', methods=['POST'])
def start_quiz():
    test_id = int(request.form['test_id'])
    timer_value = int(request.form['test_duration'])

    data = get_test_data(test_id)
    
    return render_template('test_section/quiz.html', row_data=data, index=0, timer_value=timer_value, username = session['username'])

@quiz_bp.route('/submit', methods=['POST'])
def submit():
    # global test_id
    username = session['username']
    test_id = int(request.form['test_id'])
    
    total_correct = int(request.form['total_score'])

    add_users_data(username, request.form)

    data = show_users_data('student', username, test_id)

    return render_template('test_section/result.html', row_data = data, total_correct = total_correct, username = username) 

