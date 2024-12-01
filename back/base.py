from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

# nom de la base 
db_name = "librairie"  
db = client[db_name]


db.abonnes.insert_one({"nom": "Ben Ali", "prenom": "Yasmine", "Adresse": "Rue les fleurs", "Date_dinscription": "25/10/2024", "Liste_emprunts_cours" : "Test", "historique_emprunts": "Test"})
db.livres.insert_one({"titre": "Le parfum", "type": "Science fiction", "Auteur": "Gustave Flaubert", "Date_publication": "18/05/2004", "Disponibilite" : "Non"})
db.emprunts.insert_one({"abonne": "Test", "Document_emprunte": "Test", "Date_emprunt": "12/11/2024", "Date_retour_prevue" : "16/11/2024", "statut_emprunts": "Test"})



print(f"Database '{db_name}' created successfully with a sample document.")