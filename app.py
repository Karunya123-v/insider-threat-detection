from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():

    # Safe path for dataset (important for Render)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "dataset.csv")

    # Load dataset
    df = pd.read_csv(file_path)

    # Ensure required column exists
    if 'Suspicious_Flag' not in df.columns:
        df['Suspicious_Flag'] = 'Normal'

    # Summary stats
    total_employees = len(df)
    suspicious_count = (df['Suspicious_Flag'] == 'Suspicious').sum()
    normal_count = total_employees - suspicious_count
    suspicious_percent = round((suspicious_count / total_employees) * 100, 2) if total_employees > 0 else 0

    # Table data
    results = list(zip(df['Employee_ID'], df['Suspicious_Flag']))

    # Top 50 for chart
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

# Required for Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)