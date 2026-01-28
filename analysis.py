# analysis.py
import pandas as pd

data = {
    "user": ["A", "B", "C", "D"],
    "score": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nStatistics:")
print(df.describe())
