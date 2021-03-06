'''
Created on May 6, 2015

@author: root
'''
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): # Handler for the applications root URL
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug = True)
'''
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
    app.run(debug = True)
    
    