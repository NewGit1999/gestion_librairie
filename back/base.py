from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

# nom de la base 
db_name = "librairie"  
db = client[db_name]


db.abonnes.insert_one({"nom": "Ben Ali", "prenom": "Yasmine", "Adresse": "Rue les fleurs", "Date_dinscription": "25/10/2024", "Liste_emprunts_cours" : "Test", "historique_emprunts": "Test"})
db.livres.insert_one({"titre": "Le parfum", "type": "Science fiction", "Auteur": "Gustave Flaubert", "Date de publication": "18/05/2004", "Disponibilte" : "Non"})
db.emprunts.insert_one({"abonne": "Test", "Document emprunte": "Test", "Date demprunt": "12/11/2024", "Date de retour prevue" : "16/11/2024", "statut de lemprunts": "Test"})



print(f"Database '{db_name}' created successfully with a sample document.")