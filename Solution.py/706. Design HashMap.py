class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashList = [None] * 1000001
        self.k = 1000001

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.k
        self.hashList[index] = value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.k
        if self.hashList[index] is not None:
            return self.hashList[index]
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.k
        self.hashList[index] = None
