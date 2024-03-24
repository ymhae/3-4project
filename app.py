from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key_here'

class QuestionnaireForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    short_term_goals = TextAreaField('Short Term Goals', validators=[DataRequired()])
    long_term_goals = TextAreaField('Long Term Goals', validators=[DataRequired()])
    satisfaction_level = SelectField('Satisfaction Level', choices=[('1', 'Very Satisfied'), ('2', 'Satisfied'), ('3', 'Neutral'), ('4', 'Dissatisfied'), ('5', 'Very Dissatisfied')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/info')
def info():
    return render_template('InformationPage.html')

@app.route('/data-collection', methods=['GET', 'POST'])
def data_collection():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        with open('submissions.txt', 'a') as file:
            file.write(f"{form.name.data}, {form.student_number.data}, {form.email.data}, {form.short_term_goals.data}, {form.long_term_goals.data}, {form.satisfaction_level.data}\n")
        flash('Form submitted successfully!')
        return redirect(url_for('data_collection'))
    return render_template('DataCollectionPage.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
