from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


# Initialisation de Flask
app = Flask(__name__, static_folder='front/static', template_folder='front/template')

client = MongoClient("mongodb://localhost:27017/")
db = client["librairie"]

@app.route('/')
def home():
     # return render_template('index.html')
     abonnes = list(db.abonnes.find({}, {"_id": 0})) 
     return render_template('index.html', abonnes=abonnes) 

@app.route('/addabonne', methods=[ 'GET','POST'])
def addAbonnees():
     if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        Adresse = request.form['Adresse']
        Date_dinscription = request.form['Date_dinscription']
        Liste_emprunts_cours = request.form['Liste_emprunts_cours']
        historique_emprunts = request.form['historique_emprunts']

        db.abonnes.insert_one({
          'nom': nom,
          'prenom': prenom,
          'Adresse': Adresse,
          'Date_dinscription': Date_dinscription,
          'Liste_emprunts_cours': Liste_emprunts_cours,
          'historique_emprunts':historique_emprunts})
        return redirect(url_for('home'))

     return render_template('ajouterabonne.html')


if __name__ == "__main__":
    
    app.run(debug=True)
    
    # Démarrage de l'application Flask
    app.run(host="0.0.0.0", port=5000)

