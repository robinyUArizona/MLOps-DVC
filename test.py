import pandas as pd

Data = [
    {"name": "Robins", "Age": 28, "city": "Janakpur"},
    {"name": "Sonu", "Age": 28, "city": "Imadol"},
    {"name": "Sonam", "Age": 28, "city": "Bharathawa"},
    {"name": "Sony", "Age": 28, "city": "Bharatpur"},

]

Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv", index=False)