from flask import Flask, redirect, url_for, request, Blueprint, render_template

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def index():
    return render_template('main.html')