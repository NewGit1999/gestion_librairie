from flask import Flask, render_template
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


if __name__ == "__main__":
    
    app.run(debug=True)
    
    # Démarrage de l'application Flask
    app.run(host="0.0.0.0", port=5000)

