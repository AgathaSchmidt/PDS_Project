import pandas as pd
import os


def read_file(path=os.path.join(os.getcwd(), 'data\input\duisburg.csv')):
    # i changed the slash direction because of the windows pc i own
    try:
        df = pd.read_csv(path, index_col=0)
        return df
    except FileNotFoundError:
        print('Data file not found, path was ' + path)


def read_model():
    path = os.path.join(os.getcwd(), 'data (output/model.pkl')
    with open(path, 'rb')  as f:
        model = pickle.loeaf(f)
    return model
