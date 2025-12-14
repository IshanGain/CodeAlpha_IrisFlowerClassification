from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load Model + Label Encoder
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    le = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sepal_length = float(data['sepal_length'])
    sepal_width = float(data['sepal_width'])
    petal_length = float(data['petal_length'])
    petal_width = float(data['petal_width'])

    sample = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(sample)
    species_encoded = prediction[0]
    species = le.inverse_transform([species_encoded])[0]

    # Get probabilities
    probabilities = model.predict_proba(sample)[0]
    confidence = max(probabilities) * 100

    # Descriptions for each species
    descriptions = {
        'Iris-setosa': 'Iris Setosa is typically characterized by smaller petals compared to other species. Your measurements strongly align with this classification.',
        'Iris-versicolor': 'Iris Versicolor features medium-sized petals and is known for its versatility in various environments. The model identifies this as the most likely species.',
        'Iris-virginica': 'Iris Virginica has the largest petals among the three species and often grows in wetland areas. Your input matches this distinctive profile.'
    }

    return jsonify({
        'species': species,
        'confidence': round(confidence, 1),
        'description': descriptions.get(species, 'Prediction complete.')
    })

if __name__ == '__main__':
    app.run(debug=True)
