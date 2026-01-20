import os 
import sys
import json
import pymongo

from dotenv import load_dotenv
load_dotenv()
uri = os.getenv('uri')

import numpy as np
import pandas as pd
from network_security.exceptions.exceptions import CustomException
from network_security.logging.logging import logging

class Network_data:
    def __init__(self):
        try:
            pass
        except Exception as e :
            raise CustomException(e,sys)
    
    def cv_to_json(self, path):
        try:
            data = pd.read_csv(path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient='records')
            return records
        except Exception as e:
            raise CustomException(e, sys)
    
    def insert_data(self,records,db,coll):
        try:
            self.mongo_client = pymongo.MongoClient(uri)
            self.database = self.mongo_client[db]
            self.coll = self.database[coll]
            
            # Insert in smaller batches
            batch_size = 5000
            total = 0
            for i in range(0, len(records), batch_size):
                batch = records[i:i+batch_size]
                self.coll.insert_many(batch)
                total += len(batch)
                print(f"Inserted {total}/{len(records)}")
            
            return total
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    file_path = r'Network_data\dataset_full.csv'
    db = 'KRISHAI'
    Collection = 'Network_data'
    
    print("Starting...")
    network_obj = Network_data()
    
    print("Reading CSV...")
    record = network_obj.cv_to_json(path=file_path)
    print(f"Total records: {len(record)}")
    
    print("Inserting to MongoDB...")
    no_of_records = network_obj.insert_data(record, db, Collection)
    
    print(f"✓ Success! Inserted {no_of_records} records")