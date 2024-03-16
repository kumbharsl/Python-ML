from google.cloud import firestore
import json

#firestore database configuration
credentials_path = './setup/c2w-demo-c2484-firebase-adminsdk-5cutm-8700a47d9b.json'
with open(credentials_path) as json_file:
    credentials_info = json.load(json_file)
db = firestore.Client.from_service_account_info(credentials_info)