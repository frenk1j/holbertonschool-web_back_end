#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def nginx_logs_stats(mongo_collection):
    """Print stats about Nginx logs."""
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = mongo_collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")
    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    nginx_logs_stats(nginx_collection)
