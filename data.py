import pandas as pd


class Dataset():
    def __init__(self, path='Датасет + описание\diabetes_BRFSS2015.csv'):
        self.df = pd.read_csv(path)
