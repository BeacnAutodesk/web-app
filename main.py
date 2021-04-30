from flask import Flask, render_template, url_for, redirect, request
#import registration & login classes
from forms import RegistrationForm, LoginForm, AnalysisForm
import analysis_script 
import sys

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e7287d2ce8d0bf55531b13e259d60718'

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

@app.route('/analysis', methods=('GET', 'POST'))
def analysis():
    form = AnalysisForm()
    if form.validate_on_submit():
        print('Hello world!', file=sys.stderr)
        print("data", form.product_name.data)
        print(type(form.product_name.data))

        product_name = form.product_name.data
        material_type = form.material_type.data
        material_density = form.material_density.data
        process_type = form.process_type.data
        mass = form.mass.data
        box_size = form.box_size.data

        r = analysis_script.main_analysis(product_name, material_type, material_density, 
                                        process_type, box_size, mass)
        return render_template('lca_results.html', title = 'Analysis', lca_list=r)

    else:
        print(form.errors, file=sys.stderr)
    return render_template('lca.html', title = 'Analysis', form = form)

# @app.route('/results')
# def results():

#     # product_name = "Carbon Black Steel Bolt"
#     # material_type = "Grade 5 Carbon Steel"
#     # material_density = 8000
#     # process_type = -1
#     # box_size = 0.00000036
#     # mass = 0.001
    

#     r = analysis_script.main_analysis(product_name, material_type, material_density, 
#                                         process_type, box_size, mass)
#     return render_template('lca_results.html', title = 'Analysis', lca_list=r)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


#only runs in debug mode if you run directly 
if __name__ == '__main__':
    app.run(debug=True)
