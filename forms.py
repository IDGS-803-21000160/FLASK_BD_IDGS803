from wtforms import Form
from wtforms  import StringField,IntegerField,EmailField,RadioField
from wtforms import validators

class UserForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa nombre valido')
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa Apellido paterno valido')
    ])
    amaterno=StringField('amaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa Apellido materno valido')
    ])
    edad=IntegerField('edad',[
        validators.DataRequired(message='El campo es requerido'),
        validators.number_range(min=1,max=20,message='Ingresa edad valida')
    ])
    correo=EmailField('correo',[
        validators.Email(message='Ingresa edad valida')
    ])
    
    
class DictionaryWord(Form):
    palabraEspanol=StringField('Palabra en Espanol',[
        validators.DataRequired(message='El campo es requerido')
    ])
    palabraIngles=StringField('Palabra en Ingles',[
        validators.DataRequired(message='El campo es requerido')
    ])
    

class ConsultDict(Form):
    palabraConsult=StringField('Palabra a consultar')
    options=RadioField('',choices=[(0,'Ingles'),(1,'Español')]);