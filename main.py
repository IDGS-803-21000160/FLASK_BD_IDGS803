from flask import Flask, render_template,request,Response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
import forms
from flask import flash

from config import DevelopmentConfig
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()
app.secret_key='esta es la clave secreta'

@app.route("/index",methods=["GET","POST"])
def index():
    alum_form=forms.UserForm2(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=alum_form.nombre.data,
                     apaterno=alum_form.apaterno.data,
                     email=alum_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html",form=alum_form)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    alumn_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn_form.id.data=request.args.get('id')
        alumn_form.nombre.data=alum1.nombre
        alumn_form.apaterno.data=alum1.apaterno
        alumn_form.email.data=alum1.email
    if request.method=='POST':
        id=alumn_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    
    return render_template("eliminar.html",form=alumn_form)

@app.route("/modificar",methods=["GET","POST"])
def modificar():
    alumn_form=forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn_form.id.data=request.args.get('id')
        alumn_form.nombre.data=alum1.nombre
        alumn_form.apaterno.data=alum1.apaterno
        alumn_form.email.data=alum1.email
    if request.method=='POST':
        id=alumn_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=alumn_form.nombre.data
        alum1.apaterno=alumn_form.apaterno.data
        alum1.email=alumn_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect('ABC_Completo')
    
    return render_template("modificar.html",form=alumn_form)

@app.route("/ABC_Completo",methods=["GET","POST"])
def ABC_Completo():
    alum_form=forms.UserForm2(request.form)
    alumnos=Alumnos.query.all()
    return render_template("ABC_Completo.html",alumnos=alumnos)

#Funcion que nos permite manejar el error 404 y mandar lo que queramos con el html
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    nom=''
    apa=''
    ama=''
    alum_form=forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
        print("Nombre : {} ".format(nom)) 
        print("Apellido paterno : {} ".format(apa))        
        print("Apelllido materno  : {} ".format(ama)) 
    
    return render_template("alumnos.html",form=alum_form,nom=nom)


if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()