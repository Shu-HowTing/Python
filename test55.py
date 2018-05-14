# -*- coding: utf-8 -*-
# Author: 小狼狗

class Node(object):
    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._nextnode:
                node = node._nextnode
            node._nextnode = item
            self.length += 1

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node._nextnode and j < index:
            node = node._nextnode
        j += 1
        return node.value
n = ChainTable()
n.append(5)
n.append(8)
#print(n.value)
print(n.getItem(1))
