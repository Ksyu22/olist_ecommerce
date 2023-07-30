from  fastapi import FastAPI
import pandas as pd
import requests

from scripts.parameters import LOCAL_DATA_PATH


app = FastAPI()


@app.get("/dataset/{name}")
def build_dataset(name):
    df = pd.read_csv(f'{LOCAL_DATA_PATH}/olist_{name}_dataset.csv').fillna('').to_dict()
    return df
