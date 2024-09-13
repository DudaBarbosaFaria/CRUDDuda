#verifico a pasta do progeto
#git remote -v
#git pull origin master (ou main)
#clonar o projeto --> git clone https://caminho.do.projeto
#instalar extensão python
#abrir terminal e verificar se abre (.venv), caso não abra --> ctrl + shitf + p
#digitar enviroment e criar um ambiente virtual

#pip install flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flasl-Script
#pip install pymysql
#flask db init

#flask db migrate -m "Migração Inicial"
#flask db upgrate
#executo quando minhas tabelas não estão criadas no banco de dados ^


from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Eventos
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Eventos"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route("/eventos")
def eventos():
    u = Eventos.query.all()
    return render_template("eventos_lista.html", dados=u)

@app.route("/eventos/add")
def eventos_add():
    return render_template('eventos_add.html')

@app.route("/eventos/save", methods=['POST'])
def eventos_save():
    nome = request.form.get('nome')
    data = request.form.get('data')
    local = request.form.get('local')
    if nome and data and local:
        eventos = Eventos(nome, data, local)
        db.session.add(eventos)
        db.session.commit()
        flash('Evento marcado com sucesso!!!')
        return redirect('/eventos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/eventos/add')

@app.route("/eventos/remove/<int:id_eventos>")
def eventos_remove(id_eventos):
    eventos = Eventos.query.get(id_eventos)
    if eventos:
        db.session.delete(eventos)
        db.session.commit()
        flash("Evento cancelado com sucesso!!")
        return redirect("/eventos")
    else:  
        flash("Caminho Incorreto")
        return redirect("/eventos")

@app.route("/eventos/edita/<int:id_eventos>")
def eventos_edita(id_eventos):
    eventos = Eventos.query.get(id_eventos)
    return render_template("eventos_edita.html", dados=id_eventos)

@app.route("/eventos/editasave", methods=["POST"])
def eventos_editasave():
    nome = request.form.get('nome')
    data = request.form.get('data')
    local = request.form.get('local')
    id_eventos = request.form.get('id_eventos')
    if id_eventos and nome and data and local:
        eventos = Eventos.query.get('id_eventos')
        eventos.id_eventos = id_eventos
        eventos.nome = nome
        eventos.data = data
        eventos.local = local
        db.session.commit()
        flash("Evento atualizados com sucesso!")
        return redirect("/eventos")
    else:
        flash("Faltando dados!!!")
        return redirect("/eventos")@app.route("/eventos/editasave", methods=["POST"])
   


if __name__ == '__main__':
    app.run()
