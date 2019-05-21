from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from projetc6.models import Eleve, Classe



class ClasseForm(FlaskForm):

    nomcl = StringField('Classe',
                        validators=[DataRequired(),Length(min=2, max=20)])   
    submit = SubmitField('Ajouter')

class EleveForm(FlaskForm):
    nom=StringField('Nom',validators=[DataRequired(),Length(min=2, max=20)])
    prenom=StringField('Prenom',validators=[DataRequired(),Length(min=2, max=20)])
    adresse=StringField('Adresse',validators=[DataRequired(),Length(min=2, max=30)])
    telphone=StringField('Telephone',validators=[DataRequired(),Length(min=5, max=20)])
    datenaiss=DateField('Date de naissance',validators=[DataRequired()])
    submit = SubmitField('Valider')



