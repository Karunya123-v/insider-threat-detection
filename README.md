# Insider Threat Detection System using Cybersecurity AI

## AIM
To design an AI-based system that detects insider threats within an organization using employee activity data and presents results through a professional web-based dashboard.

---

## Objectives
- Detect suspicious employee behavior based on activity metrics  
- Visualize results with interactive tables and charts  
- Develop a web-based dashboard using Flask for intuitive reporting  

---

## Tools & Technologies
- **Programming Language:** Python 3.x  
- **Web Framework:** Flask  
- **Data Processing & ML:** Pandas, scikit-learn (Random Forest Classifier)  
- **Dashboard & Visualization:** Bootstrap, Chart.js  

---

## Dataset
- Employee activity CSV file with sample columns:  
  `Employee_ID`, `File_Access_Count`, `Emails_Sent`, `Login_Hours`, `Suspicious_Flag`  

---

## System Architecture
1. **Upload dataset** via the home page (`index.html`)  
2. **Predict suspicious activities** using ML model  
3. **Generate dashboard** (`dashboard.html`) containing:  
   - Summary cards (total employees, suspicious count, suspicious %)  
   - Table with Normal/Suspicious status (color-coded)  
   - Pie chart for Normal vs Suspicious  
   - Bar chart for employee activity metrics  

---

## Algorithm
1. Load dataset using pandas  
2. Preprocess data if necessary  
3. Train a Random Forest model (if labels are available)  
4. Predict Suspicious/Normal for each employee  
5. Compute summary statistics for dashboard  
6. Pass processed data to dashboard template  
7. Display results via interactive cards, table, and charts  

---

## Output / Screenshots
**Sample Dashboard:**  

- Summary cards showing total employees, suspicious count, and percentage  
- Color-coded table: green = Normal, red = Suspicious  
- Pie chart of Normal vs Suspicious  
- Bar chart for files accessed per employee  

*(Place screenshots in `screenshots/` folder and reference them here)*

---

## Conclusion
- Efficient detection of insider threats using AI  
- Web-based dashboard provides clear and interactive visualization  
- Easily extendable to real-time monitoring for organizations  

---
Author:
Karunya Vaithiyanathan
