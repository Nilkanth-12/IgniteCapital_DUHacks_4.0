from pymongo import MongoClient

DATABASES = {
    "default": {
        "ENGINE": "djongo",  # Djongo is outdated, we will use pymongo instead
        "NAME": "ignitecapital",  # Replace with your database name
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb://localhost:27017/",  # Change if using a cloud database
            "username": "",  # Add if authentication is needed
            "password": "",
            "authSource": "admin",
        }
    }
}

MONGO_CLIENT = MongoClient("mongodb://localhost:27017/")  # Update if using cloud DB
MONGO_DB = MONGO_CLIENT["ignitecapital"]  # Change to your actual MongoDB database name
ALLOWED_HOSTS = ['*']  
DEBUG = True
