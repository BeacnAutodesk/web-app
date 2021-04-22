from flask import Flask, render_template, url_for
#import registration & login classes
from forms import RegistrationForm, LoginForm 
app = Flask(__name__)

app.config['SECRET KEY'] = 'e7287d2ce8d0bf55531b13e259d60718'

posts = [
    {
        'author' : 'Birks Sachdev',
        'title' : 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2020'    
    },

    {
        'author' : 'Abhay Aggarwal',
        'title' : 'Blog Post 2',
        'content': 'First Post Content',
        'date_posted': 'April 21, 2020'    
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)
    #form = form -> access to form

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


#only runs in debug mode if you run directly 
if __name__ == '__main__':
    app.run(debug=True)
