#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection using kwargs."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document using kwargs and return its ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
