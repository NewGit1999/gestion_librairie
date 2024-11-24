from flask import Flask, render_template

# Initialisation de Flask
app = Flask(__name__, static_folder='front/static', template_folder='front/template')



@app.route('/')
def home():
     return render_template('index.html')

if __name__ == "__main__":
    
    app.run(debug=True)
    
    # Démarrage de l'application Flask
    app.run(host="0.0.0.0", port=5000)

