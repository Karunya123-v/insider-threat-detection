import pandas as pd
import random

# ---------------------------
# CONFIG: How many employees
# ---------------------------
num_employees = 200  # You can change this to 500, 1000, etc.

# ---------------------------
# GENERATE DATA
# ---------------------------
data = []

for i in range(1, num_employees + 1):
    emp_id = f"E{i:03d}"           # E001, E002, ...
    files = random.randint(5, 100) # Files accessed
    emails = random.randint(5, 80) # Emails sent
    hours = random.randint(6, 14)  # Login hours
    # 10% chance to be suspicious
    flag = "Suspicious" if random.random() < 0.1 else "Normal"
    data.append([emp_id, files, emails, hours, flag])

# ---------------------------
# CREATE DATAFRAME
# ---------------------------
df = pd.DataFrame(
    data,
    columns=['Employee_ID', 'File_Access_Count', 'Emails_Sent', 'Login_Hours', 'Suspicious_Flag']
)

# ---------------------------
# SAVE CSV
# ---------------------------
df.to_csv("dataset.csv", index=False)
print(f"dataset.csv generated with {num_employees} employees!")