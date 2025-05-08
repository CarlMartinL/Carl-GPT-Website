from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

from website.Chat_GPT.Chat_gpt import chat_with_gpt


@auth.route('/',methods=['POST'])
def respond():
    global messages

    initialMessage = "Carl-GPT: Hi, I am CarlGPT. What do you want to talk about?"
    messages = [initialMessage]

    #User respnse
    userReply = get_user_reply()
    messages.append(userReply)

    #Chat response
    chatReply = 'Carl-GPT: '+chat_with_gpt(f'Here is the previous messages we have. You are Carl-GPT, and You is the user: {messages}, Your job is to answer the users newest text which is: {userReply}')
    messages.append(chatReply)

    #Return all information
    return render_template("carl-gpt.html", boolean=True,messages=messages)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 2:
            flash('Name must be greater than 2 characters.',category='error')
        elif password1 != password2:
            flash('The passwords dont match',category='error')
        elif len(password1) < 7:
            flash('password must be greater than 7 characters',category='error')
        else:
            #add user to database
            flash('Account created', category='success')
    return render_template("sign_up.html")


#
#Used to retrieve the text that the user submitted to the website
#
def get_user_reply():
    user_input = request.form['user_input']
    return f'You : {user_input}'
