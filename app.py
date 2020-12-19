import flask
import pandas as pd
from pickle import load
import warnings
warnings.filterwarnings("ignore")

with open(f'model/model.pkl', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        date_mutation = flask.request.form['date_mutation']
        surface_reelle_bati = flask.request.form['surface_reelle_bati']
        nombre_pieces_principales = flask.request.form['nombre_pieces_principales']
        longitude = flask.request.form['longitude']
        latitude = flask.request.form['latitude']
        distance_mer = flask.request.form['distance_mer']

        input_data = {'date_mutation': [date_mutation],
                      'surface_reelle_bati': [surface_reelle_bati],
                      'nombre_pieces_principales': [nombre_pieces_principales],
                      'longitude':[longitude],
                      'latitude': [latitude],
                      'distance_mer':[distance_mer]}

        input_variables = pd.DataFrame(input_data)

        predictions = model.predict(input_variables)
        print(predictions)

        return flask.render_template('main.html', original_input={'Date mutation': date_mutation, 'Surface': surface_reelle_bati, 'Nombre de pièces': nombre_pieces_principales, 'Longitude': longitude, 'Latitude': latitude, 'Distance': distance_mer},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
