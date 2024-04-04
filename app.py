from flask import Flask, render_template
from backend.login import login_bp
from backend.admin import admin_bp
from backend.profile import profile_bp
from backend.student import student_bp

app = Flask(__name__)

app.secret_key = 'this_is_truely_secret'

app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(student_bp)

if __name__ == '__main__':
    app.run(debug=True)