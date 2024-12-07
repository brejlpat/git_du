class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.nodes = []

    def __repr__(self):
        node = self.head
        self.nodes = []
        while node is not None:
            self.nodes.append(node.data)
            node = node.next
        self.nodes.append("None")
        return " -> ".join(self.nodes)

    def put(self, data):
        # put data in a queue
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get(self, index):
        # get data from a queue
        print(f"Node on index {index} is: {self.nodes[index]}")
        return self.nodes[index]

    def empty(self):
        # is queue empty?
        if self.head is None:
            print("Queue is empty")
            return True
        print("Queue is not empty")
        return False

    def full(self):
        # is queue full?
        if len(self.nodes)-1 == 10:
            print("Queue is full")
            return True
        print("Queue is not full")
        return False

    def size(self):
        # what is the size of a queue?
        print(f"Size of the Queue is: {len(self.nodes) - 1}")
        return len(self.nodes) - 1

    def last_node(self):
        last_head = self.head
        while last_head and last_head.next:
            last_head = last_head.next
        self.tail = last_head
        print(f"Last node is: {last_head}")
        return last_head


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"{self.data}"


rada = Queue()
rada.put("1")
rada.put("2")
rada.put("3")
rada.put("4")
rada.put("5")
rada.put("6")
rada.put("7")
rada.put("8")
rada.put("9")
rada.put("10")
print(rada)
print(rada.empty())
print(rada.size())
print(rada.full())
print(rada.get(5))
print(rada.last_node())
