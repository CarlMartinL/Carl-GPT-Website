from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    #
    #
    #
    return render_template("carl-gpt.html", messages= ["Carl-GPT: Hi, I am CarlGPT. What do you want to talk about?"])

