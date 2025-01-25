import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Temp': [30, 22, 28, 35, 33, 25, 27, 32, 31],
    'Humidity': [60, 65, 55, 40, 45, 70, 50, 60, 55],
    'Wind speed': [10, 12, 18, 17, 18, 16, 14, 11, 19],  # Fixed length to match others
    'Pressure': [1015, 1017, 1019, 1016, 1013, 1012, 1011, 1018, 1012]
}

df = pd.DataFrame(data)

# Scatter plot Temp vs Humidity
plt.figure(figsize=(8,6))
plt.scatter(df['Temp'], df['Humidity'], color='blue', label='Temp vs Humidity')
plt.title('Temp vs Humidity')
plt.xlabel('Temp')
plt.ylabel('Humidity')
plt.grid(True)
plt.legend()

# Pairplot without the 'hue' argument
sns.pairplot(df)
plt.show()
