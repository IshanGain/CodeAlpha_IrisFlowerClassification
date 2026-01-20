IRIS FLOWER CLASSIFICATION (INTERNSHIP PROJECT BY CODEALPHA):
- This project uses a Decision Tree classifier to predict iris flower species (Setosa, Versicolor, Virginica) from sepal and petal measurements. The model learns from four input features—SepalLengthCm, SepalWidthCm, PetalLengthCm, and PetalWidthCm—to classify the Species of an iris flower.

LIVE DEMO:
- https://irisflowerclassification-hxy5.onrender.com/

FEATURES:
- Uses DecisionTreeClassifier for multi‑class classification on the Iris dataset.
- Reads data from Iris.csv with clearly separated feature and label columns.
- Jupyter notebook (IrisClassification.ipynb) for data exploration, model training, and evaluation.
- Saved model (iris_model.pkl) and label encoder (label_encoder.pkl) for reuse without retraining.
- Simple front‑end/web interface via app.py and templates/ to predict species from user inputs.

INSTALLATION:
- git clone https://github.com/IshanGain/IrisFlowerClassification.git
- cd IrisFlowerClassification
- pip install -r requirements.txt

RUN LOCALLY (OPTIONAL):
- python app.py

- Then open the local URL shown in the terminal to use the app on your machine.

PROJECT STRUCTURE:
- IrisFlowerClassification/
- ├── Iris.csv                  # Dataset
- ├── IrisClassification.ipynb  # EDA + model training notebook
- ├── app.py                    # Web app for predictions
- ├── iris_model.pkl            # Trained Decision Tree model
- ├── label_encoder.pkl         # Label encoder for species
- ├── templates/                # HTML templates for UI
- ├── requirements.txt          # Dependencies
- └── README.md                 # Project documentation


