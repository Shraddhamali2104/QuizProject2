from flask import Blueprint, render_template, session, request, redirect, url_for
from backend.database import view_profile_data, update_profile_database

profile_bp = Blueprint('profile', __name__)

images_folder = "/user_images"  # Replace with your images folder path

@profile_bp.route('/view_profile/<username>')
def index(username): #Displays the profile page for a specific user.
    data = view_profile_data(username)
    # print(data)
    return render_template('profiles/view_profile.html', data = data, username = username)
    
@profile_bp.route('/edit_profile', methods=['GET'])
def edit_profile():
    # print("usr ty 2 : " + user_type)
    # user = session['user']
    username = session['username']
    data = view_profile_data(username)
    return render_template('profiles/edit_profile.html',data = data, username = username)

@profile_bp.route('/update_profile', methods=['POST'])
def update_profile():
    # global user_type
  
    username = session['username']
    # print(request.form)

    update_profile_database(username, request.form)
    data = view_profile_data(username)
    # return redirect(url_for('profile.index', username=username))
    return render_template('profiles/view_profile.html', data = data, username = username)
