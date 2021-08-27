from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormularioRegistro(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length (min=4, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Senha',
                           validators=[DataRequired()])
    password_confirm = PasswordField('Confirme Senha',
                           validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Enviar')

class FormularioLogin(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Senha',
                           validators=[DataRequired()])
    password_confirm = PasswordField('Confirme Senha',
                           validators=[DataRequired(), EqualTo(password)])
    remember = BooleanField('Lembrar de Mim')
    submit = SubmitField('Login')