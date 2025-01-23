import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
data = {
    'square_feet_area': [8500, 9600, np.nan, 11250, np.nan, 9550, 14260, np.nan, 13820, 11500],
    'Year_built': [2003, 1976, 2001, np.nan, 1998, 2000, 2006, 1978, 1950, np.nan],
    'over_all_condition': [5, 8, 6, 7, np.nan, 7, np.nan, np.nan, np.nan, np.nan],
    'ready_to_move': ['Yes', 'No', 'Yes', np.nan, 'No', np.nan, 'Yes', 'Yes', 'No', 'Yes'],
    'Sale_price': [200000, 180000, 215000, 250000, 210000, 190000, 23000, 225000, 220000, 240000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

numeric_imputer = SimpleImputer(strategy='mean')
df[['square_feet_area', 'Year_built', 'over_all_condition']] = numeric_imputer.fit_transform(df[['square_feet_area', 'Year_built', 'over_all_condition']])

print("\nDataFrame after Imputation:")
print(df)