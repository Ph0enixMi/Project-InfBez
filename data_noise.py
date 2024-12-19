import pandas as pd
import numpy as np


df = pd.read_csv('Датасет + описание\diabetes_BRFSS2015.csv')


def add_noise_random_values(column, noise_level=0.1, change_ratio=0.1):
    n_changes = int(len(column) * change_ratio)
    indices_to_change = np.random.choice(column.index, size=n_changes, replace=False)
    noise = np.random.normal(0, noise_level, size=n_changes)
    column.loc[indices_to_change] = column.loc[indices_to_change] + noise
    return column

for column in df.columns:
    if df[column].dtype in ['float64', 'int64']:
        df[column] = add_noise_random_values(df[column], noise_level=0.1, change_ratio=0.2)

df.to_csv('Датасет с аномалиями\modified_dataset.csv', index=False)
