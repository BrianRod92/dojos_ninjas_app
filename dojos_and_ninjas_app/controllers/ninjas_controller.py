from flask import render_template, redirect, request, session
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.ninjas_model import Ninjas
from dojos_and_ninjas_app.models.dojos_model import Dojos

@app.route('/dojo-show/<int:id>')
def dojo_show(id):
    
    ninjas = Ninjas.get_with_dojos(id)
    dojos = Dojos.get_one(id)
    
    return render_template('dojo_show.html', ninjas=ninjas, dojos=dojos)



@app.route('/new-ninja')
def new_ninja():
    dojos = Dojos.get_all()
    return render_template('newninja.html', dojos=dojos)



@app.route('/create-ninja', methods=['POST'])
def create_ninja():
    
    Ninjas.create(request.form)
    dojo_id = request.form['dojo_id']

    return redirect(f'/dojo-show/{dojo_id}')