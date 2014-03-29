from flask import Flask, render_template, request, redirect, url_for
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

from forms import AForm

app = Flask(__name__)

@app.route('/')
def listar():
    return render_template("listar.html")

@app.route('/cadastrar/')
def cadastrar():
    return render_template("cadastrar.html")
 
@app.route('/<registro_id>/edit/', methods=['GET', 'POST'])
def editar():
    return render_template("editar.html") 

if __name__ == '__main__':
    app.run()

  