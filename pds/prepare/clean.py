from ..io import read_file
import pandas as pd

df = read_file()


def delete(df):
    print('Deleting the rows with nan values...')
    df.dropna(inplace=True)
    print('Deleting duplicate columns...(since p_spot, p_place_type and p_bike contain the same information')
    df['p_place_type', 'p_bike'].drop(axis=1, inplace=True)
    print('Deleting b_bike_type_row, since it is unimportant for our analysis')
    df['b_bike_type'].drop(axis=1, inplace=True)
    print('new dataframe:', df)
