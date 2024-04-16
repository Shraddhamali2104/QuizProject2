import matplotlib

matplotlib.use("Agg")  # Use the Agg backend

from flask import Blueprint, render_template, session, request, redirect, url_for
from backend.database import show_users_data, get_testid_score_report
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

student_bp = Blueprint("student", __name__)


@student_bp.route("/student")
def index():
    return render_template("student/home.html", username=session["username"])


@student_bp.route("/view_previous_tests")
def view_previous_tests():

    data = show_users_data(session["user"], session["username"])

    return render_template(
        "student/view_test_history.html", row_data=data, username=session["username"]
    )


@student_bp.route("/generate_student_report", methods=["GET"])
def generate_student_report():

    # Generate some sample data
    tuples_list = get_testid_score_report(session["username"])

    if tuples_list == False:
        return "Unable generate report"

    # Separate lists for first and second elements
    x = [t[0] for t in tuples_list]
    y = [t[1] for t in tuples_list]

    # Define threshold values
    green_threshold = 7
    blue_threshold = 4

    # Create a scatter plot with colored points
    for i in range(len(x)):
        color = "red"  # Default color is red

        # Determine color based on the y value
        if y[i] > green_threshold:
            color = "green"
        elif blue_threshold <= y[i] <= green_threshold:
            color = "blue"

        # plt.scatter(x[i], y[i], color=color)
        plt.scatter(
            x[i],
            y[i],
            color=color,
            s=150,
            marker="o",
            alpha=0.9,
            edgecolors="black",
            linewidths=0.7,
        )

    plt.xlabel("Subject")
    plt.ylabel("Score")
    plt.title("Subject Vs Score")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Encode the plot as base64 string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Close the plot to free up memory
    plt.close()

    # Pass the base64 encoded plot data to the template
    return render_template("student/generate_student_report.html", plot_data=plot_data)
