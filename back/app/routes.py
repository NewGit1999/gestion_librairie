from flask import Blueprint, request, jsonify
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["librairie"]

# Blueprint pour les routes 'abonne'
abonne_bp = Blueprint('abonnes', __name__)

@abonne_bp.route('/abonne', methods=['POST'])
def create_abonne():
    data = request.json
    db.abonnes.insert_one(data)
    return jsonify({"message": "Abonné créé avec succès !"}), 201

@abonne_bp.route('/abonne', methods=['GET'])
def get_abonnes():
    abonnes = list(db.abonnes.find({}, {"_id": 0}))
    return jsonify(abonnes), 200

@abonne_bp.route('/abonne/<nom>', methods=['PUT'])
def update_abonne(nom):
    data = request.json
    db.abonnes.update_one({"nom": nom}, {"$set": data})
    return jsonify({"message": "Abonné mis à jour avec succès !"}), 200

@abonne_bp.route('/abonne/<nom>', methods=['DELETE'])
def delete_abonne(nom):
    db.abonnes.delete_one({"nom": nom})
    return jsonify({"message": "Abonné supprimé avec succès !"}), 200
