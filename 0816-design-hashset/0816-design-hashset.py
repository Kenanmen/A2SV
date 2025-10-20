class MyHashSet:

    def __init__(self):
        self._items = {}

    def add(self, key: int) -> None:
        self._items[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self._items[key]

    def contains(self, key: int) -> bool:
        return key in self._items
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)