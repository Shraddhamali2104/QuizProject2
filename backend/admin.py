from flask import Blueprint, render_template, session, request
from flask import redirect
from flask import url_for
from backend.database import get_test_details, add_questions_to_database, add_test_details, get_question_number_from_test_details, check_details_to_update_table, show_users_data, get_test_id, view_students_list, remove_student_DB

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
   

@admin_bp.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    # username = request.args.get('username')
    if request.method == 'GET':
        return render_template('admin/add_subject.html', username = session['username'])
    else:
        test_id = get_test_id(request.form)
        username = session['username']

        if(add_test_details(request.form)):
            
            return redirect(url_for('admin.subject_data'))
        else:
            return "unable to add data to the test_details table"
            # return redirect(url_for('admin.index'))

   

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
        pass

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
    

@admin_bp.route('/users_list', methods=['GET'])
def user_list():
    if 'username' in session:
        username = session['username']
        # Fetch user data using the updated show_users_data function
        data = view_students_list()
        if data:
            return render_template('admin/user_list.html', user_data=data, username=username)
        else:
            return "No users found."
    else:
        return redirect(url_for('login.index'))


@admin_bp.route('/remove_student', methods=['GET'])
def remove_student():
    if 'username' in session:
        if request.method == 'GET':
            data = view_students_list()
            if data:
                return render_template('admin/remove_student.html', user_data = data)
            else:
                return "No users found."
        else:
            user_id = request.form['user_id']
            if(remove_student_DB(user_id)):
                return redirect(url_for('admin.user_list'))
            else:
                return "unable to delete"
    else:
        return redirect(url_for('login.index'))

@admin_bp.route('/subject_data', methods=['GET', 'POST'])
def subject_data():
    if 'username' in session:
        if request.method == 'GET':
            data = get_test_details()
            if data:
                return render_template('admin/subject_data.html', data = data)
            else:
                return "No data found."
        else:
            pass
    else:
        return redirect(url_for('login.index'))



