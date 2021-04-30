from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
        validators = [DataRequired(), Email()])
    password = PasswordField('Password', 
        validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
        validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', 
        validators = [DataRequired(), Email()])
    password = PasswordField('Password', 
        validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    #allow usernames between 2 and 20 char
    #use validators

class AnalysisForm(FlaskForm):
    # product_name = StringField('Product Name', 
    #         validators = [DataRequired("Fail 1")])
    product_name = SelectField('Product Name', choices=[("Carbon Black Steel Bolt", "Carbon Black Steel Bolt")])
    # material_type = StringField('Material Type', 
    #         validators = [DataRequired("Fail 2")])
    material_type = SelectField('Material Type', choices=[("Grade 5 Carbon Steel", "Carbon Steel")])
    material_density = FloatField('Material Density (kg/m\N{SUPERSCRIPT THREE})', 
            validators = [DataRequired("Fail 3")])
    p_type = SelectField('Process Type', choices=[(-1, 'Subtractive'), (1, 'Additive')], coerce=float)
    mass = FloatField('Mass of Component (kg)', 
            validators = [DataRequired("Fail 5")])
    box_size = FloatField('Size of Component (m\N{SUPERSCRIPT THREE})', 
            validators = [DataRequired("Fail 6")])
    submit = SubmitField('Complete LCA')
