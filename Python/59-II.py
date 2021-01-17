class Node:
    def __init__(self, val):
        self.val = val
        self.front = None
        self.next = None

class MaxQueue:

    def __init__(self):
        self.start = Node(None)
        self.end = Node(None)
        self.max = []      # Monotonic queue
        self.num = 0

    def max_value(self) -> int:
        if self.num == 0:
            return -1
        else:
            return self.max[0]

    def push_back(self, value: int) -> None:
        node = Node(value)

        if self.num == 0:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            node.front = self.end
            self.end = self.end.next

        while len(self.max) > 0 and value > self.max[-1]:
            self.max.pop()
        self.max.append(value)

        self.num += 1

    def pop_front(self) -> int:
        res = self.start.val
        if self.num == 0:
            return -1
        elif self.num == 1:
            self.start = Node(Node)
            self.end = Node(Node)
            self.max = []
        else:
            head = self.start.next
            self.start.next = None
            head.front = None

            if self.start.val == self.max[0]:
                self.max.pop(0)

            self.start = head
        self.num -= 1
        return res


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.push_back(1)
print("max", obj.max_value())
obj.push_back(5)
print("max", obj.max_value())
obj.push_back(5)
print("max", obj.max_value())
obj.push_back(3)
print("max", obj.max_value())
obj.push_back(4)
print("max", obj.max_value())
obj.push_back(2)
print("max", obj.max_value())

print(obj.pop_front())
print("max", obj.max_value())
print(obj.pop_front())
print("max", obj.max_value())
print(obj.pop_front())
print("max", obj.max_value())
print(obj.pop_front())
print("max", obj.max_value())
print(obj.pop_front())
print("max", obj.max_value())
print(obj.pop_front())
print("max", obj.max_value())
