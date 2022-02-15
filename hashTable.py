# Hash table

import hashlib
from typing import Any, Optional

class HashTable(object):
    def __init__(self) -> None:
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def hash(self, key: Any) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: Any, value: Any) -> None:
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        
        else: self.table[index].append([key, value])
    
    def print(self) -> None:
        for i in range(self.size):
            print(i, end=" ")
            for data in self.table[i]:
                print("-->", end=" ")
                print(data, end=" ")
            
            print()

    def get(self, key: Any) -> Optional[Any]:
        index = self.hash(key)
        
        for data in self.table[index]:
            if data[0] == key: return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)
    
    def __getitem__(self, key) -> Optional[Any]:
        return self.get(key)


if __name__ == "__main__":
    h = HashTable()
    h["car"] = "Tesla"
    h.add("pc", "Mac")
    h.add("sns", "YouTube")
    print(h["car"])
    h.print()
    print(h.get("1"))
