#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (25.47%)
# Total Accepted:    297.3K
# Total Submissions: 1.2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
#
class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashmap = {}
        self.rev_hashmap = {}
        self.limit = capacity
        self.start = Node(None)
        self.end = Node(None)
        self.start.next = self.end
        self.end.prev = self.start
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.start
            node.next = self.start.next
            self.start.next.prev = node
            self.start.next = node
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.hashmap:
            if (len(self.hashmap) == self.limit) and (self.limit != 0):
                node_to_del = self.end.prev
                node_to_del.prev.next = self.end
                self.end.prev = node_to_del.prev
                node_to_del.prev = None
                node_to_del.next = None
                digit = self.rev_hashmap[node_to_del]
                del self.rev_hashmap[node_to_del]
                del self.hashmap[digit]
            if self.limit != 0:
                node = Node(value)
                self.start.next.prev = node
                node.next = self.start.next
                node.prev = self.start
                self.start.next = node
                self.hashmap[key] = node
                self.rev_hashmap[node] = key
        else:
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.start
            node.next = self.start.next
            self.start.next.prev = node
            self.start.next = node
            node.value = value
                        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
