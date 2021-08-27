# save this as app.py
from flask import Flask, escape, request, render_template, url_for
from forms import FormularioRegistro, FormularioLogin

app = Flask(__name__)

app.config['SECRET-KEY']='3d0501d196d4dcf0cbda38ad11'

posts = [
    {
        'autor': 'Marcus Mesquita',
        'titulo': 'Blog Post 1',
        'conteudo': 'Conteudo do primeiro post',
        'data_post': '20 Abril, 2020'
    },
    {
        'autor': 'Tainah Comini',
        'titulo': 'Blog Post 2',
        'conteudo': 'Conteudo do segundo post',
        'data_post': '21 Abril, 2020'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/sobre')
def about():
    return render_template('about.html', title='Sobre')

@app.route('/registro')
def register():
    from = FormularioRegistro()
    return render_template('register.html', title='Registre-se', form=form)

@app.route('/login')
def login():
    from = FormularioLogin()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
