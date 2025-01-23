import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'semester': ['Sem1', 'Sem1', 'Sem1', 'Sem1', 'Sem1', 'Sem2', 'Sem2', 'Sem2', 'Sem2', 'Sem2'],
    'hours_studied': [7, 9, 4, 17, 23, 68, 92, 81, 72, 10]
}

df = pd.DataFrame(data)

# Adjust the figure size
plt.figure(figsize=(6,6))
sns.boxplot(x='semester', y='hours_studied', data=df)
plt.title('Student Performance')
plt.xlabel('Semester')
plt.ylabel('No. of Hours Studied')
plt.show()