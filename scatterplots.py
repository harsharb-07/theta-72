import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Stock_A_returns': [0.02, 0.03, -0.01, 0.04, -0.03, 0.01, 0.05, 0.02, -0.02, 0.01],
    'Stock_B_returns': [0.01, -0.02, 0.04, 0.03, 0.02, -0.01, 0.04, 0.01, 0.02, 0.01]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.scatter(df['Stock_A_returns'], df['Stock_B_returns'], color='blue', label='Returns Comparison')

plt.title('Stock A vs Stock B Returns')
plt.xlabel('Stock A Returns', fontsize=12)
plt.ylabel('Stock B Returns', fontsize=12)

plt.grid(True)
plt.legend()

plt.show()
