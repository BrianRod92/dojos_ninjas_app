from flask import render_template, redirect, request
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.dojos_model import Dojos

@app.route('/')
def index():
    
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojos.get_all()
    
    return render_template('dojos.html', dojos=dojos)


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojos.create(request.form)
    print(request.form)
    return redirect ('/')
