import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from projetc6 import app, db
from projetc6.forms import ClasseForm, EleveForm
from projetc6.models import Eleve, Classe
# from flask_login import login_user, current_user, logout_user, login_required



# beginning part classes routes
@app.route("/")
@app.route("/allclasses")
def allclasses():
	page=request.args.get('page',1,type=int)
	classes=Classe.query.order_by(Classe.nomcl.asc()).paginate(page=page,per_page=3)
	# classes=Classe.query.all()
	return render_template('allclasses.html',classes=classes)

@app.route("/ajoutcl",methods=['GET', 'POST'])
def ajoutcl():
	form=ClasseForm()
	if form.validate_on_submit():
		cl=Classe(nomcl=form.nomcl.data)
		db.session.add(cl)
		db.session.commit()
		flash('Classe ajouter avec success!', 'success')
		return redirect(url_for('allclasses'))
	return render_template('nouveau_classe.html', title='Ajouter Classe',
		form=form, legend='Nouvelle classe')

@app.route('/editclasse/<int:cl_id>', methods=['GET', 'POST'])
def update_classe(cl_id):
	classe = Classe.query.get_or_404(cl_id)
	form=ClasseForm()	
	if request.method=='POST':		
		if form.validate_on_submit():
			classe.nomcl = form.nomcl.data
			# classe.serie = form.serie.data
			db.session.commit()
			flash('Classe modifier avec Succes!', 'success')
		return redirect(url_for('allclasses'))
	else:
		form.nomcl.data = classe.nomcl
		# form.serie.data = classe.serie
		return render_template('Editclasse.html', title='Modifier Classe', 
			classe=classe, form=form, legend='Modifier Classe')	


@app.route("/classe/<int:cl_id>/delete",methods=['POST','GET'])
def delete_classe(cl_id):
	classe = Classe.query.get_or_404(cl_id)
	db.session.delete(classe)
	db.session.commit()
	flash('Classe supprimer avec Succes!', 'success')
	return redirect(url_for('allclasses'))
# end part classes routes

# beginning part eleves routes
@app.route('/ajout_elv',methods=['GET', 'POST'])
def ajout_elv():
	form=EleveForm()
	form1=ClasseForm()
	allclasses = Classe.query.all()		
	if form.validate_on_submit():
		select=request.form.get('cl_select')
		select_el=request.form.get('el_select')
		# return(str(select))
		cl=Classe.query.filter_by(nomcl=str(select)).first()	
		elv=Eleve(nom=form.nom.data,prenom=form.prenom.data,datenaiss=form.datenaiss.data,
			adresse=form.adresse.data,telphone=form.telphone.data,id_classe=cl.id)
		db.session.add(elv)
		db.session.commit()
		flash('Eleve ajouter avec success!', 'success')
		return redirect(url_for('all_eleves'))
	return render_template('nouveau_eleve.html', title='Ajouter Eleve', 
		form=form, legend='Inscription',form1=form1, allclasses=allclasses)

# all_eleves
@app.route("/all_eleves")
def all_eleves():
	page=request.args.get('page',1,type=int)
	eleves=Eleve.query.order_by(Eleve.id_classe.desc()).paginate(page=page,per_page=3)
	# eleves=Eleve.query.all()
	return render_template('all_eleves.html',eleves=eleves)
# end part classes routes