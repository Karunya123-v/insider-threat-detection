from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'dataset' not in request.files:
        return redirect('/')
    file = request.files['dataset']
    df = pd.read_csv(file)

    # Ensure Suspicious_Flag exists
    if 'Suspicious_Flag' not in df.columns:
        df['Suspicious_Flag'] = 'Normal'

    # Summary stats
    total_employees = len(df)
    suspicious_count = (df['Suspicious_Flag'] == 'Suspicious').sum()
    normal_count = total_employees - suspicious_count
    suspicious_percent = round((suspicious_count / total_employees) * 100, 2)

    # Prepare results for table
    results = list(zip(df['Employee_ID'], df['Suspicious_Flag']))

    # Top 50 employees by File_Access_Count for bar chart
    df_sorted = df.sort_values(by='File_Access_Count', ascending=False).head(50)
    employee_ids = df_sorted['Employee_ID'].tolist()
    files_accessed = df_sorted['File_Access_Count'].tolist()

    return render_template(
        'dashboard.html',
        total_employees=total_employees,
        suspicious_count=suspicious_count,
        suspicious_percent=suspicious_percent,
        normal_count=normal_count,
        results=results,
        employee_ids=employee_ids,
        files_accessed=files_accessed
    )

if __name__ == '__main__':
    app.run(debug=True)