from flask import Flask, request, render_template,Response
from flask_wtf.csrf import CSRFProtect
import forms 
from flask import flash
from flask import g
from config import DevelopmentConfig 
from models import db
from models import Alumnos
app=Flask(__name__)


app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


'''     
Decoradores o rutas
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



@app.route("/index",methods=["GET","POST"])
def index():
    alum_form=forms.UserForm2(request.form)
    
    if request.method == 'POST' and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data,
                 apaterno=alum_form.apaterno.data,
                 email=alum_form.email.data)
        
        #insert into alumnos values()
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=alum_form)


@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
    alum_form=forms.UserForm2(request.form)
    #select * from alumnos 
    alumnos=Alumnos.query.all()
    
    return render_template("ABC_Completo.html",alumno=alumnos)
   

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    
    alumn_form=forms.UserForm(request.form)
    if request.method == 'POST' and alumn_form.validate():
        nom=alumn_form.nombre.data    
        email=alumn_form.email.data    
        apaterno=alumn_form.apaterno.data   
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom)) 
        print("email: {}".format(email)) 
        print("Apellido paterno: {}".format(apaterno)) 
    return render_template("alumnos.html", form =alumn_form )
   
    
   


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()

