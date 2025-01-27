import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'Age': [25, 30, 35, 40, 45],
    'Height': [0.00, 0.25, 0.30, 0.40, 0.50],  # Fixed height values
    'Weight': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
scaler = MinMaxScaler()

# Normalize the data
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("\nNormalized DataFrame (scaled to range [0, 1]):")
print(normalized_df)