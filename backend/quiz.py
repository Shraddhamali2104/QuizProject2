from flask import Blueprint, render_template, session, request, redirect, url_for
from backend.database import (
    get_subject_namesDB,
    get_all_tests_DB,
    get_test_data,
    get_test_basic_details,
    add_result_to_user_data_DB, 
    show_users_data,
)

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/quiz", methods=["GET", "POST"])
def index():
    if "username" in session:
        if request.method == "GET":
            data = get_subject_namesDB()
            # print(data)
            if data:
                return render_template("test_section/home.html", data=data)
            else:
                return "No subjects found"
        else:
            subject = request.form["subject"]
            data = get_all_tests_DB(subject)
            if data:
                return render_template("test_section/home2.html", data=data)
            else:
                return "No test found"
    else:
        return redirect(url_for('login.index'))


@quiz_bp.route("/start_test", methods=["GET", "POST"])
def start_test():
    # return "success"
    if "username" in session:
        if request.method == "GET":
            test_id = request.args.get("test_id")
            # print(test_id)
            return render_template("test_section/instructions.html", test_id = test_id)
        else:
            test_id = request.form["test_id"]
            data = get_test_data(test_id)
            basic_data = get_test_basic_details(test_id)
            return render_template(
                "test_section/quiz.html", row_data=data, index=0, basic_data=basic_data
            )
    else:
        return redirect(url_for('login.index'))

@quiz_bp.route("/submit", methods = ['GET', 'POST'])
def submit():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            total_score = int(request.form['total_score'])
            test_id = int(request.form['test_id'])

            add_result_to_user_data_DB(request.form, username)
            data = show_users_data(session['user'], username, test_id )
            if(data):
                return render_template("test_section/result.html", total_score = total_score, data = data )
            else:
                return "unable to submit result"

        else:
            pass
    else:
        return redirect(url_for('login.index'))
