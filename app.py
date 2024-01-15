from flask import Flask, request, render_template_string

import pandas as pd

app = Flask(__name__)

# Initialisation d'un DataFrame vide avec les colonnes 'first_name' et 'last_name'

user_data = pd.DataFrame(columns=['first_name', 'last_name'])


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global user_data
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # Ajout des données de l'utilisateur dans le DataFrame
        user_data = user_data.append({'first_name': first_name, 'last_name': last_name}, ignore_index=True)


        return 'Bienvenue {} {}. Voici tous les utilisateurs enregistrés :<br>{}'.format(first_name, last_name, user_data.to_html())

    return '''
        <form method="POST">
            Prénom: <input type="text" name="first_name"><br>
            Nom: <input type="text" name="last_name"><br>
            <input type="submit" value="Envoyer">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

