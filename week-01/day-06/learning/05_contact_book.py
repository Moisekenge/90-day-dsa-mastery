"""
Day 6 - Project: CLI Contact Book
Add, search, delete, list, save/load JSON. Uses classes + error handling.
"""
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Contact:
    def __init__(self, name, phone, email):
        # TODO: Implement
        pass
    
    def __str__(self):
        pass
    
    def to_dict(self):
        pass
    
    @classmethod
    def from_dict(cls, data):
        pass


class ContactBook:
    def __init__(self, filename="contacts.json"):
        # TODO: Implement
        pass
    
    def add(self, contact):
        pass
    
    def search(self, query):
        pass
    
    def delete(self, name):
        pass
    
    def list_all(self):
        pass
    
    def save(self):
        pass
    
    def load(self):
        pass


def main():
    # TODO: CLI menu loop
    pass


if __name__ == "__main__":
    main()
