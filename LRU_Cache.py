# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# Follow up:
# Could you do both operations in O(1) time complexity?
# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 263 ms
# Your runtime beats 60.97 % of python submissions.
# Use double linked list and Dict.
class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru_cache = dict()
        self.head = node(0, 0)
        self.tail = node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru_cache:
            value = self.lru_cache[key].value
            self.put(key, value)
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lru_cache:
            self.remove(self.lru_cache[key])
        n = node(key, value)
        self.add(n)
        self.lru_cache[key] = n
        if len(self.lru_cache) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.lru_cache[n.key]

    def remove(self, n):
        p = n.prev
        p.next = n.next
        n.next.prev = p

    def add(self, n):
        p = self.tail.prev
        n.prev = p
        p.next = n
        n.next = self.tail
        self.tail.prev = n


if __name__ == '__main__':
    capacity = 1
    key, value = 'a', 1
    obj = LRUCache(capacity)
    obj.put(key, value)
    param_1 = obj.get(key)
    print(param_1)
