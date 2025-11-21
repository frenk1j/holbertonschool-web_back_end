#!/usr/bin/env python3
"""Update all topics of a school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name."""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_many(myquery, newvalues)
