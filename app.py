from flask import Flask, render_template, request
import pickle
import pandas as pd
from transformer import Transformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

dialect_mapper = {
    0: "اللهجة الليبية",
    1: "اللهجة المغربية",
    2: "اللهجة المصرية",
    3: "اللهجة الليبنانية",
    4: "اللهجة السودانية"
}

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/detect', methods=['POST'])
def detect():
    text = request.form['text']
    dialect = dialect_mapper[model.predict(pd.Series([text]))[0]]
    return render_template('home.html', message={text}, dialect=dialect)


if __name__ == '__main__':
    app.run(debug=True)
