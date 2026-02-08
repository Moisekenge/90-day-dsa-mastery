"""
Hash Table (Separate Chaining)
Day 12 | O(1) avg, O(n) worst.
"""


class Implementation:
    def __init__(self):
        # TODO: Initialize
        pass

    def _hash(self, key):
        """hash(key) % capacity"""
        # TODO: Implement
        pass

    def put(self, key, value):
        """Insert/update. Resize if load > 0.75"""
        # TODO: Implement
        pass

    def get(self, key):
        """Retrieve value. Raise KeyError if missing"""
        # TODO: Implement
        pass

    def remove(self, key):
        """Delete key. Raise KeyError if missing"""
        # TODO: Implement
        pass

    def contains(self, key):
        """Check existence. O(1) avg"""
        # TODO: Implement
        pass

    def _resize(self):
        """Double capacity, rehash all entries"""
        # TODO: Implement
        pass


if __name__ == "__main__":
    # TODO: Test every method
    print("Hash Table (Separate Chaining) - All tests passed!")
