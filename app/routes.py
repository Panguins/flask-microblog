from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Shitty day in Portland...'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Avengers sucks.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)