import os
import pymongo

from abc import ABC, abstractmethod


MONGO_URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017/courses")


class AbstractMongoRepository(ABC):
    def __init__(self) -> None:
        self.mongo_url = MONGO_URL
        self.client = pymongo.MongoClient(self.mongo_url)
        self.database = self.client.courses

    def save(self, aggregate_root: object) -> None:
        self.database.get_collection(
            self.collection_name()
        ).insert_one(aggregate_root.to_primitive())

    @abstractmethod
    def collection_name(self):
        ...
