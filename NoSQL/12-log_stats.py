#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def main():
    """Prints log statistics from MongoDB collection logs.nginx."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_query = {"method": "GET", "path": "/status"}
    status_count = collection.count_documents(status_query)
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
