#https://leetcode.com/problems/lru-cache/submissions/
#146. LRU Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def add(self, key, value):
        node = Node(key, value)
        if self.head:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        else:
            self.head = self.tail = node 
            
        return node

    def pop_head(self):
        if not self.head:
            raise Exception("There is no head")
            
        node = self.head     
        self.remove_node(self.head)
        return node
    
    
    def remove_node(self, node):
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.previous = None
        elif self.tail == node:
            self.tail = self.tail.previous
            self.tail.next = None
            node.previous = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.linked_list = LinkedList()

        
    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self.linked_list.remove_node(node)
        new_node = self.linked_list.add(node.key, node.value)
        self.table[key] = new_node
        return new_node.value
    

    def put(self, key: int, value: int) -> None:    
        if key in self.table:
            node = self.table[key]
            self.linked_list.remove_node(node)
            new_node = self.linked_list.add(node.key, value)
            self.table[key] = new_node
            return
        
        if len(self.table) == self.capacity:
            head = self.linked_list.pop_head()
            self.table.pop(head.key)

        
        node = self.linked_list.add(key, value)
        self.table[key] = node


if __name__ == '__main__':
    
    vals = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]


    cache = LRUCache(2)
    for val in vals[1:]:
        if len(val) == 1:
            print(cache.get(val[0]))
        else:
            print(cache.put(val[0], val[1]))



# ["LRUCache","put","put","get","put"]
# [[2],[1,1],[2,2],[1],[3,3]]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)