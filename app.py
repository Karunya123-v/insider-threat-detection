from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['dataset']
    df = pd.read_csv(file)
    
    # ML: Predict Suspicious vs Normal
    if 'Suspicious_Flag' in df.columns:
        X = df.drop('Suspicious_Flag', axis=1)
        y = df['Suspicious_Flag'].apply(lambda x: 1 if x=='Suspicious' else 0)
    else:
        X = df
        y = None

    model = RandomForestClassifier()
    if y is not None:
        model.fit(X, y)
        df['Prediction'] = model.predict(X)
        df['Prediction'] = df['Prediction'].apply(lambda x: 'Suspicious' if x==1 else 'Normal')
    else:
        df['Prediction'] = 'Normal'

    # Dashboard stats
    total_employees = len(df)
    suspicious_count = (df['Prediction']=='Suspicious').sum()
    suspicious_percent = round((suspicious_count/total_employees)*100,2)
    normal_count = total_employees - suspicious_count

    employee_ids = df.iloc[:,0].tolist()       # First column = Employee_ID
    files_accessed = df.iloc[:,1].tolist()     # Second column = File_Access_Count

    results = list(zip(df.iloc[:,0], df['Prediction']))
    
    return render_template('dashboard.html', 
                           results=results,
                           total_employees=total_employees,
                           suspicious_count=suspicious_count,
                           suspicious_percent=suspicious_percent,
                           normal_count=normal_count,
                           employee_ids=employee_ids,
                           files_accessed=files_accessed)

if __name__ == '__main__':
    app.run(debug=True)