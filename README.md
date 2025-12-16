IRIS FLOWER CLASSIFICATION:
This project uses a Decision Tree classifier to predict iris flower species (Setosa, Versicolor, Virginica) from sepal and petal measurements. The model learns from four input features—SepalLengthCm, SepalWidthCm, PetalLengthCm, and PetalWidthCm—to classify the Species of an iris flower.

FEATURES:
- Uses DecisionTreeClassifier for multi‑class classification on the Iris dataset.
- Reads data from Iris.csv with clearly separated feature and label columns.
- Jupyter notebook (IrisClassification.ipynb) for data exploration, model training, and evaluation.
- Saved model (iris_model.pkl) and label encoder (label_encoder.pkl) for reuse without retraining.
- Simple front‑end/web interface via app.py and templates/ to predict species from user inputs.

INSTALLATION:
git clone https://github.com/your-username/CodeAlpha_IrisFlowerClassification.git
cd CodeAlpha_IrisFlowerClassification
pip install -r requirements.txt

