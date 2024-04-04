from flask import Blueprint, render_template, session, request
from flask import redirect
from flask import url_for
from backend.database import get_test_details, add_questions_to_database, add_test_details, get_question_number_from_test_details, check_details_to_update_table, show_users_data, get_test_id

admin_bp = Blueprint('admin', __name__) 

@admin_bp.route('/admin') #Displays the admin main page.
def index():
    if 'username' in session:
        # print(getTestNumberData())
        # index = 0  # Set the initial value of index
        return render_template('admin/home1.html', username = session['username'])
    else:
        return redirect(url_for('login.index'))

@admin_bp.route('/view_data_admin', methods=['GET'])
def view_data_admin():
    username = session['username']
    data = show_users_data('admin', username)#fetch data for the admin.
    # print(data)
    return render_template('admin/view_data_admin.html', row_data = data, username = username)
   

@admin_bp.route('/add_subject', methods=['GET'])
def add_subject():
    # username = request.args.get('username')
    return render_template('admin/add_subject.html', data = get_test_details(), username = session['username'])
   

@admin_bp.route('/add_questions', methods=['GET'])
def add_questions_get():
    test_id = get_test_id(request.args)
    username = session['username']
    #function in Database to add new subject in the database.
    if(request.args.get('submit_type') == 'update'):
        if(check_details_to_update_table(request.args)):#validate the details for updating the table.
            
            
            q_n = get_question_number_from_test_details(test_id)
            return render_template('admin/add_questions.html', test_id = test_id, question_no = q_n, username = username )

        return "incorrect details to Update table, try again, or create new table"
    else:
        if(add_test_details(request.args)):

            return render_template('admin/add_questions.html', test_id = test_id, question_no = 1, username = username)
        else:
            return "unable to add data to the test_details table"
            # return redirect(url_for('admin.index'))

@admin_bp.route('/add_questions', methods=['POST']) #Handles the submission of questions form.
def add_questions():
    if(add_questions_to_database(request.form)):
        test_id = request.form['test_id']
        q_n = get_question_number_from_test_details(test_id)
        username = session['username']

        # question_number = 0 
        return render_template('admin/add_questions.html', test_id = test_id, question_no = q_n, username = username )
    else:
        return "Unable to add questions to database, Go back and try again"
    
@admin_bp.route('/users_list')

@admin_bp.route('/user_list', methods=['GET'])
def user_list():
    if 'username' in session:
        username = session['username']
        # Fetch user data using the updated show_users_data function
        data = show_users_data('admin', username)
        if data:
            return render_template('admin/user_list.html', user_data=data, username=username)
        else:
            return "No users found."
    else:
        return redirect(url_for('login.index'))

