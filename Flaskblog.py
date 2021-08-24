# save this as app.py
from flask import Flask, escape, request, render_template

app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
