from flask import Flask, redirect, url_for, request, Blueprint, render_template, session
from backend.database import setup_initial_tables, insert_initial_data, authenticate_user, signup_user
import os

images_folder_DB = "/user_images"  # Replace with your images folder path
images_folder_local = "static/user_images"  # Replace with your images folder path

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def index():
    setup_initial_tables()
    insert_initial_data()
    return render_template('main.html')

@login_bp.route('/login/<user>', methods=['GET'])
def login_get(user):
    # user = request.args.get('user')
    session['user'] = user
    if user in ['student', 'admin', 'guest']:
        return render_template('login_signup_section/login.html', user = user)
    else:
        return redirect(url_for('login.index'))
    
@login_bp.route('/login',methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    user = session['user']
    print(user)

    auth_result = authenticate_user(user, username, password)
    if auth_result is True:
        session['username'] = username
        if user == 'admin':
            return redirect(url_for('admin.index'))
        elif user == 'student':
            return redirect(url_for('student.index'))
    elif auth_result is False:
        return "Password incorrect. Please try again."
    else:
        return "User not found. Please register first."
    
@login_bp.route('/signup', methods=['GET'])
def signup():
    # user = request.args.get('user')
    user = session['user']
    # print(user)
    return render_template('login_signup_section/signup.html', user = user)

@login_bp.route('/signup', methods=['POST']) #form submission for user sign up 
def signup_submit():
    username = request.form['username']
    image_file = request.files["profile_pic"]
    image_path_DB = False
    # print(request.files)  # Added for debugging

    if username and image_file:
        # print("enter this if condition")
        # Construct filename using username and extension
        filename = f"{username}.jpg"  # Adjust extension as needed
        # Construct image path only if there's an image file
        image_path_DB = os.path.join(images_folder_DB, filename)
        image_path_local = os.path.join(images_folder_local, filename)

        # Save image
        image_file.save(image_path_local)

    # Use image_path only if it's defined (within the if block or after)
    # if image_path:  # Check if image_path has a value before using it
    try:#handle potential exceptions that may occur during the signup process.
        signup_user(request.form, image_path_DB)#saving the user data to the database.
        
        return render_template('login_signup_section/login.html', user = session['user'])
    except Exception as e:
        print("Error occurred:", e)
        return "An error occurred. Please try again later."
    