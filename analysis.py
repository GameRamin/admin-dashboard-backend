# analysis.py
import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "score": [80, 90, 75]
}

df = pd.DataFrame(data)
print(df.describe())
