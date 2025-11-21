#!/usr/bin/env python3
"""Return the list of schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic."""
    value = {"topics": topic}
    return mongo_collection.find(value)
