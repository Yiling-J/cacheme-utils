from typing import Optional

class TinyLfu:
    def __init__(self, size: int): ...
    def set(self, key: str) -> Optional[str]: ...
    def remove(self, key: str): ...
    def access(self, key: str): ...

class Lru:
    def __init__(self, size: int): ...
    def set(self, key: str) -> Optional[str]: ...
    def remove(self, key: str): ...
    def access(self, key: str): ...

class BloomFilter:
    def put(self, key: str): ...
    def contains(self, key: str): ...
