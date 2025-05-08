from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("carl-gpt.html", messages= ["Carl-GPT: Hi, I am CarlGPT. What do you want to talk about?"])

