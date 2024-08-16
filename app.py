import json
from flask import Flask, render_template, request
from Disease_Diagnostic_ES import DiseaseDiagnosticExpertSystem  # Import the expert system

app = Flask(__name__)

def load_symptoms():
    with open('symptoms.json') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    symptoms_config = load_symptoms()
    medications = []

    if request.method == 'POST':
        symptoms = {}
        for key in symptoms_config.keys():
            symptoms[key] = 'yes' if request.form.get(key) == 'on' else 'no'

        # Create an instance of the expert system and run the diagnosis
        engine = DiseaseDiagnosticExpertSystem()
        diagnosis, medications = engine.diagnose(symptoms)  # Run the inference engine and get the diagnosis

    return render_template('index.html', diagnosis=diagnosis, symptoms=symptoms_config, medications=medications)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask web server
