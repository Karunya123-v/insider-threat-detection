from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/detect', methods=['POST'])
def detect():

    file = request.files['file']
    data = pd.read_csv(file)

    model = IsolationForest(contamination=0.2)

    X = data[['login_time','files_accessed','data_downloaded']]

    model.fit(X)

    data['Threat'] = model.predict(X)

    data['Threat'] = data['Threat'].replace({1:'Normal',-1:'Suspicious'})

    table = data.to_html()

    return render_template("result.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)