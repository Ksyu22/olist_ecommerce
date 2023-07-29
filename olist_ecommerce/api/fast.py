from  fastapi import FastAPI
import pandas as pd
import requests

from scripts.parameters import LOCAL_DATA_PATH


app = FastAPI()

@app.get("/customers")
def build_customers():
    df = pd.read_csv(f'{LOCAL_DATA_PATH}/olist_customers_dataset.csv').fillna('').to_dict()
    return df

@app.get("/geolocation")
def build_geolocation():
    df = pd.read_csv(f'{LOCAL_DATA_PATH}/olist_geolocation_dataset.csv').fillna('').to_dict()
    return df

@app.get("/sellers")
def build_geolocation():
    df = pd.read_csv(f'{LOCAL_DATA_PATH}/olist_sellers_dataset.csv').fillna('').to_dict()
    return df

@app.get("/orders")
def build_geolocation():
    df = pd.read_csv(f'{LOCAL_DATA_PATH}/olist_orders_dataset.csv').fillna('').to_dict()
    return df
