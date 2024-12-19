import pandas as pd
import numpy as np

df = pd.read_csv('Датасет + описание\diabetes_BRFSS2015.csv')

def add_noise_random_values(column, change_ratio=0.5):
    max_value = column.max()
    n_changes = int(len(column) * change_ratio)
    indices_to_change = np.random.choice(column.index, size=n_changes, replace=False)
    
    random_values = np.random.randint(0, max_value + 1, size=n_changes)
    column.loc[indices_to_change] = random_values
    return column

for column in df.columns:
    if df[column].dtype in ['float64', 'int64']:
        df[column] = add_noise_random_values(df[column], change_ratio=0.3)

df.to_csv(r'Датасет с аномалиями\modified_dataset.csv', index=False)