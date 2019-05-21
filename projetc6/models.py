from datetime import datetime
from projetc6 import db
from flask_login import UserMixin



class Classe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nomcl = db.Column(db.String(20), unique=True, nullable=False)
	# serie = db.Column(db.String(20), unique=False, nullable=False)	
	eleves = db.relationship('Eleve', backref='classe', lazy=True)

	def __repr__(self):
		return f"Classe('{self.nomcl}','{self.serie}')"

class Eleve(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(20), unique=False, nullable=False)
	prenom = db.Column(db.String(20), unique=False, nullable=False)
	datenaiss = db.Column(db.DateTime, nullable=False)
	adresse = db.Column(db.String(20), nullable=False)
	telphone = db.Column(db.String(20), nullable=False)
	
	id_classe = db.Column(db.Integer, db.ForeignKey('classe.id'), nullable=False)

	def __repr__(self):
		return f"Eleve('{self.nom}','{self.prenom}','{self.datenaiss}','{self.adresse}','{self.telphone}')"
