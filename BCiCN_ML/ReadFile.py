import pandas as pd
import xgboost as xgb


def getData(path):
    return pd.read_csv(path)

def getCol(path):
    col = open(path,'r').read().split('\n')
    return col

def getModel(path):
    my_model = xgb.XGBRegressor()
    my_model.load_model(path) 
    return my_model

def to_output():
    output =  pd.DataFrame()
