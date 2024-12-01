from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["librairie"]

#ABONNES
# Blueprint pour les routes 'abonne'
abonne_bp = Blueprint('abonnes', __name__)

@abonne_bp.route('/addabonne', methods=['POST'])
def create_abonne():
    data = {
        "nom": request.form.get("nom"),
        "prenom": request.form.get("prenom"),
        
        "Adresse": request.form.get("Adresse"),
        "Liste_emprunts_cours": request.form.get("Liste_emprunts_courss"),
        "historique_emprunts": request.form.get("historique_emprunts"),
        "Date_dinscription": request.form.get("Date_dinscription")
    }
    # data = request.json
    db.abonnes.insert_one(data)
    return jsonify({"message": "Abonné créé avec succès !"}), 201
    return redirect(url_for('/'))

@abonne_bp.route('/abonne', methods=['GET'])
def get_abonnes():
    abonnes = list(db.abonnes.find({}, {"_id": 0}))
    return jsonify(abonnes), 200

@abonne_bp.route('/abonne/<nom>', methods=['PUT'])
def update_abonne(nom):
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée fournie"}), 400
    db.abonnes.update_one({"nom": nom}, {"$set": data})
    return jsonify({"message": "Abonné mis à jour avec succès !"}), 200

@abonne_bp.route('/abonne/<nom>', methods=['DELETE'])
def delete_abonne(nom):
    db.abonnes.delete_one({"nom": nom})
    return jsonify({"message": "Abonné supprimé avec succès !"}), 200

#LIVRES

livre_bp = Blueprint('livres', __name__)
@abonne_bp.route('/addLivre', methods=['POST'])
def create_abonne():
    data = {
        "titre": request.form.get("titre"),
        "type": request.form.get("type"),
        
        "Auteur": request.form.get("Auteur"),
        "Date_publication": request.form.get("Date_publication"),
        "Disponibilite": request.form.get("Disponibilite"),
        
    }
    # data = request.json
    db.livres.insert_one(data)
    return jsonify({"message": "Livre créé avec succès !"}), 201
    return redirect(url_for('/livres'))

@livre_bp.route('/livre', methods=['GET'])
def get_livres():
    livres = list(db.livres.find({}, {"_id": 0}))
    return jsonify(livres), 200

@livre_bp.route('/livre/<titre>', methods=['DELETE'])
def delete_livre(titre):
    db.livres.delete_one({"titre": titre})
    return jsonify({"message": "Livre supprimé avec succès !"}), 200

    #EMPRUNTS

emprunt_bp = Blueprint('emprunts', __name__)