from flask import Blueprint, render_template, session, request, redirect, url_for
from backend.database import show_users_data

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def index():
    return render_template('student/home.html', username = session['username'])


    
@student_bp.route('/view_previous_tests')
def view_previous_tests():
   
    data = show_users_data(session['user'], session['username'])
    # print(data)
    # return "success"
    return render_template('student/view_test_history.html', row_data = data, username = session['username'])

