import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json")

plt.scatter(df['Displacement'], df['Miles_per_Gallon'])
plt.xlabel("Displacement")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara kapasitas mesin dengan Miles per gallon")
plt.show()