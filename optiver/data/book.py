import pandas as pd


class Book:
    def __init__(self, path_train, path_test):
        self._path_train = path_train
        self._path_test = path_test

        self.raw_train = pd.read_parquet(self._path_train)
        self.raw_test = pd.read_parquet(self._path_train)
