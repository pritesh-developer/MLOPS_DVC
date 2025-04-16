import pandas as pd
import os


data = {"Namn":["Anna", "Jony", "Priyanka", "Pritesh"],
"Age":[23,33,35,36],
"City":["Chennai", "Pune", "Leeds","Leeds"]}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "data.csv")
df.to_csv(file_path, index=False)

print("CSV file created successfully")
 