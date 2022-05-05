from flask import render_template, url_for, flash, redirect
from flaskBlog import app
from flaskBlog.forms import RegistrationForm, LoginForm
from flaskBlog.models import User, Post

# this a list that containes dictionaries containing information of post blog
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
# same as
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html', 
                            title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'{form.email.data} have been logged in :', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessfull please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
