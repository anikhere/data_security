from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = "yourusername"
password = "password"

uri = f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@cluster0.btjj58s.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)