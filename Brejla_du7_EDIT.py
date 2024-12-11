class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.nodes = []

    def __repr__(self):
        node = self.head
        self.nodes = []

        # create list of all Nodes in the Queue
        while node is not None:
            self.nodes.append(node.data)
            node = node.next
        self.nodes.append("None")

        # print the Queue
        return " -> ".join(self.nodes)

    def put(self, data):
        # put data in a queue
        new_node = Node(data)

        # new Node becomes a head, if there is nothing in the Queue
        if self.head is None:
            self.head = new_node
            return

        # else, now Node is added to the Queue on the last position
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get(self, index):
        # get data from a queue according to its index
        print(f"Node on index {index} is: {self.nodes[index]}")
        return self.nodes[index]

    def empty(self):
        # if there is None in the Queue only (it is empty), code returns True
        if self.head is None:
            print("Queue is empty")
            return True

        # else False (not empty)
        print("Queue is not empty")
        return False

    def full(self):
        # for max 10 nodes in the Queue
        # if there is 10 nodes, code returns True
        if len(self.nodes)-1 == 10:
            print("Queue is full")
            return True

        # else False
        print("Queue is not full")
        return False

    def size(self):
        # returns the size of the Queue
        print(f"Size of the Queue is: {len(self.nodes) - 1}")
        return len(self.nodes) - 1

    def last_node(self):
        # returns the last Node in the Queue
        # first element as last_head
        last_head = self.head
        # until there will be next element, it will save next Nodes in last_head
        while last_head and last_head.next:
            last_head = last_head.next

        # return the last_head
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
rada.put("11")
print(rada)
print(rada.empty())
print(rada.size())
print(rada.full())
print(rada.get(5))
print(rada.last_node())
