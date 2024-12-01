from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient


# Initialisation de Flask
app = Flask(__name__, static_folder='front/static', template_folder='front/template')

client = MongoClient("mongodb://localhost:27017/")
db = client["librairie"]

#ABONNES

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

@app.route('/delete_abonne/<nom>', methods=['POST'])
def delete_abonne(nom):
    # Tenter de supprimer l'abonné
    result = db.abonnes.delete_one({"nom": nom})
    
    # Vérifier si l'abonné existait
    if result.deleted_count == 0:
        return "Abonne introuvable", 404

    # Rediriger vers la liste des abonnés après suppression
    return redirect(url_for('home'))

@app.route('/update_abonne/<nom>', methods=['POST'])
def update_abonne(nom):
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    Adresse = request.form.get('Adresse')
    Liste_emprunts_cours = request.form.get('Liste_emprunts_cours')
    historique_emprunts = request.form.get('historique_emprunts')
    Date_dinscription = request.form.get('Date_dinscription')

    abonne = db.abonnes.find_one({"nom": nom})
    
    if not abonne:
        return jsonify({"error": "Abonné introuvable"}), 404

    db.abonnes.update_one(
        {"nom": nom},
        {"$set": {
            "nom": nom,
            "prenom": prenom,
            "adresse": adresse,
            "Liste_emprunts_cours": Liste_emprunts_cours,
            "historique_emprunts": historique_emprunts,
            "Date_dinscription": Date_dinscription
        }}
    )

    return redirect(url_for('home'))  # Redirige vers la liste des abonnés

    #LIVRES

@app.route('/livres')
def livres():
    livres = list(db.livres.find({}, {"_id": 0})) 
    return render_template('livres.html', livres=livres)

@app.route('/addLivre', methods=[ 'GET','POST'])
def addLivres():
     if request.method == 'POST':
        # Récupérer les données du formulaire
        titre = request.form['titre']
        type = request.form['type']
        Auteur = request.form['Auteur']
        Date_publication = request.form['Date_publication']
        Disponibilite = request.form['Disponibilite']
        

        db.livres.insert_one({
          'titre': titre,
          'type': type,
          'Auteur': Auteur,
          'Date_publication': Date_publication,
          'Disponibilite': Disponibilite,
          })
        return redirect(url_for('livres'))

     return render_template('ajouterlivre.html')

@app.route('/delete_livre/<titre>', methods=['POST'])
def delete_livre(titre):
    # Tenter de supprimer l'abonné
    result = db.livres.delete_one({"titre": titre})
    
    # Vérifier si l'abonné existait
    if result.deleted_count == 0:
        return "Livre introuvable", 404

    # Rediriger vers la liste des abonnés après suppression
    return redirect(url_for('livres'))


    #EMPRUNTS
@app.route('/emprunts')
def emprunts():
    emprunts = list(db.emprunts.find({}, {"_id": 0})) 
    return render_template('emprunts.html', emprunts=emprunts)






if __name__ == "__main__":
    
    app.run(debug=True)
    
    # Démarrage de l'application Flask
    app.run(host="0.0.0.0", port=5000)

