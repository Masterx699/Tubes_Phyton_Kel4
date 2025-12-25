import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("X:\Code\Tubes_Phyton_Kel4\Dataset\Raw\cars2.json")

plt.scatter(df['Weight_in_lbs'], df['Miles_per_Gallon'])
plt.xlabel("Berat")
plt.ylabel("Miles Per Gallon")
plt.title("Hubungan antara berat kendaraan dengan Miles per gallon")
plt.show()