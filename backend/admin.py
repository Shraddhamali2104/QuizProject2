from flask import Blueprint, render_template, session, request
from flask import redirect
from flask import url_for
from backend.database import (
    get_test_details,
    add_test_details,
    show_users_data,
    view_students_list,
    remove_student_DB,
    update_subjectDB,
    remove_subjectDB,
    add_questionsDB,
)
from backend.plots import plot_data_admin, plot_data_admin2

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")  # Displays the admin main page.
def index():
    if "username" in session:
        # print(getTestNumberData())
        # index = 0  # Set the initial value of index
        return render_template("admin/home1.html", username=session["username"])
    else:
        return redirect(url_for("login.index"))


@admin_bp.route("/view_data_admin", methods=["GET"])
def view_data_admin():
    username = session["username"]
    data = show_users_data("admin", username)  # fetch data for the admin.
    # print(data)
    return render_template(
        "admin/view_data_admin.html",
        row_data=data,
        username=username,
        plot_data=plot_data_admin(data),
        plot_data2=plot_data_admin2(data),
    )


@admin_bp.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    # username = request.args.get('username')
    if request.method == "GET":
        return render_template("admin/add_subject.html", username=session["username"])
    else:
        # test_id = get_test_id(request.form)
        # username = session['username']

        if add_test_details(request.form):

            return redirect(url_for("admin.subject_data"))
        else:
            return "unable to add data to the test_details table"
            # return redirect(url_for('admin.index'))


@admin_bp.route("/update_subject", methods=["GET", "POST"])
def update_subject():
    if request.method == "GET":
        return render_template("admin/update_subject.html")

    else:
        if update_subjectDB(request.form):
            return redirect(url_for("admin.subject_data"))
        else:
            return "Error occured"


@admin_bp.route("/add_questions", methods=["GET", "POST"])
def add_questions():
    if request.method == "GET":
        return render_template("admin/add_questions.html")
    else:
        if add_questionsDB(request.form):
            return redirect(url_for("admin.index"))
        else:
            return "Unable to add question"


@admin_bp.route("/users_list", methods=["GET"])
def user_list():
    if "username" in session:
        username = session["username"]
        # Fetch user data using the updated show_users_data function
        data = view_students_list()
        if data:
            return render_template(
                "admin/user_list.html", user_data=data, username=username
            )
        else:
            return "No users found."
    else:
        return redirect(url_for("login.index"))


@admin_bp.route("/remove_student", methods=["GET", "POST"])
def remove_student():
    if "username" in session:
        if request.method == "GET":
            # data = view_students_list()
            # if data:
            return render_template("admin/remove_student.html")
            # else:
            # return "No users found."
        else:
            user_id = request.form["user_id"]
            if remove_student_DB(user_id):
                return redirect(url_for("admin.user_list"))
            else:
                return "unable to delete"
    else:
        return redirect(url_for("login.index"))


@admin_bp.route("/subject_data", methods=["GET", "POST"])
def subject_data():
    if "username" in session:
        if request.method == "GET":
            data = get_test_details()
            if data:
                return render_template("admin/subject_data.html", data=data)
            else:
                return "No Subjects found."
        else:
            pass
    else:
        return redirect(url_for("login.index"))


@admin_bp.route("/remove_subject", methods=["GET", "POST"])
def remove_subject():
    if request.method == "GET":
        return render_template("admin/remove_subject.html")
    else:
        if remove_subjectDB(request.form):
            return redirect(url_for("admin.subject_data"))
        else:
            return "Unable to remove test "
