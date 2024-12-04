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
    #nom = request.form.get('nom')
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
            #"nom": nom,
            "prenom": prenom,
            "Adresse": Adresse,
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

@app.route('/addEmprunt', methods=['GET', 'POST'])
def addEmprunt():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        abonne_nom_prenom = request.form['abonne']
        Document_emprunte = request.form['Document_emprunte']
        Date_emprunt = request.form['Date_emprunt']
        Date_retour_prevue = request.form['Date_retour_prevue']
        statut_emprunts = request.form['statut_emprunts']

        nom, prenom = abonne_nom_prenom.split(' ')

        abonne = db.abonnes.find_one({'nom': nom, 'prenom': prenom})
        livre = db.livres.find_one({'titre': Document_emprunte})

        db.emprunts.insert_one({
            'abonne': f"{nom} {prenom}",
            'Document_emprunte': Document_emprunte,
            'Date_emprunt': Date_emprunt,
            'Date_retour_prevue': Date_retour_prevue,
            'statut_emprunts': statut_emprunts,
        })

        return redirect(url_for('emprunts'))

   
    abonnes = list(db.abonnes.find({}, {"_id": 0, "nom": 1, "prenom": 1}))
    livres = list(db.livres.find({}, {"_id": 0, "titre": 1}))
    return render_template('AddEmprunts.html', abonnes=abonnes, livres=livres)

@app.route('/delete_emprunt/<Date_emprunt>', methods=['POST'])
def delete_emprunt(Date_emprunt):
    # Tenter de supprimer l'abonné
    result = db.emprunts.delete_one({"Date_emprunt": Date_emprunt})
    
    # Vérifier si l'abonné existait
    if result.deleted_count == 0:
        return "Emprunt introuvable", 404

    # Rediriger vers la liste des abonnés après suppression
    return redirect(url_for('emprunts'))
    





if __name__ == "__main__":
    
    app.run(debug=True)
    
    # Démarrage de l'application Flask
    app.run(host="0.0.0.0", port=5000)

