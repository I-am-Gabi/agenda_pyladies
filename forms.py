from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField
from wtforms import validators

class AForm(Form):
	nome = TextField('Nome', [validators.Length(min=4, max=25)])
	telefone = StringField('Telefone')
    	email = TextField('Email', [validators.Length(min=6, max=35)]) 