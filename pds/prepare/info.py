import pandas as pd
import numpy as np

from ..io import read_file

df = read_file()
column_names = df.columns


def df_info(df):
        print('Number of rows in our df:', len(df))
        print('Number of columns in our df:', len(df.columns))
        print('Datatypes for each column:')
        for i in column_names:
            print("\033[1m" + i + "\033[0m", np.dtype(df[i]))



def col_info(df):
    for i in column_names:
        print("\033[1m" + i + "\033[0m")
        print('Unique values of the column', i, ':', df[i].unique())
        print('Number of unique columns of the column', i, ':', len(df[i].unique()), '\n')