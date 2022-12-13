import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
print("Loading enviroment varibale from .env file")
load_dotenv()

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://admin:getSOMETHINGnew_009@cluster0.2sdtbef.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH="https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"ROWS AND COLUMNS: {df.shape}")

    #convert dataframe to json so that we can dump these records in mongo db
    df.reset_index(drop=True,inplace=True)

    json_records = list(json.loads(df.T.to_json()).values())
    print(json_records[0]) 

    #insert converted json record json to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)