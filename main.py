from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/accueil')
def accueil():
    return render_template("accueil.html")

@app.route('/listes')
def listes():
    return render_template("listes.html")

@app.route('/produits')
def produits():
    return render_template("produits.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
