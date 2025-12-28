import pandas as pd

df = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json")
df = df.dropna()

print(df.describe())


