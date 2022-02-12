import hashlib
from typing import Any


class HashTable(object):
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: Any) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base = 16) % 10

    def add(self, key: Any, value: Any) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        
        else: self.table[index].append([key, value])
    
    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")

            print()
    
    def get(self, key: Any) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key: return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key) -> Any:
        return self.get(key)

if __name__ == "__main__":
    h = HashTable()
    h["car"]  = "Tesla"
    h["pc"] = "Mac"
    h.add("sns", "YouTube")
    h.print()
    h.get("car")
    h.get("aaa")
    print(h["sns"])

