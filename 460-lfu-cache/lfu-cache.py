class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.freq=1
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self._size=0

    def add_to_head(self,node:Node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self._size+=1

    def remove(self,node:Node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self._size-=1

    def remove_tail(self)->Node:
        if self._size==0:
            return None
        lru_node=self.tail.prev
        self.remove(lru_node)
        return lru_node

    def __len__(self):
        return self._size

class LFUCache:

    def __init__(self,capacity:int):
        self.capacity=capacity
        self.cache={}        
        self.freq_map={}    
        self.min_freq=0

    def _update_freq(self,node:Node):
        freq=node.freq
        self.freq_map[freq].remove(node)
        if freq==self.min_freq and len(self.freq_map[freq])==0:
            self.min_freq+=1
            
        node.freq+=1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq]=DoublyLinkedList()
        self.freq_map[node.freq].add_to_head(node)

    def get(self,key:int)->int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._update_freq(node)
        return node.val

    def put(self,key:int,value:int)->None:
        if self.capacity==0:
            return

        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self._update_freq(node)
        else:
            if len(self.cache)>=self.capacity:
                lru_list=self.freq_map[self.min_freq]
                evicted_node=lru_list.remove_tail()
                del self.cache[evicted_node.key]

            new_node=Node(key,value)
            self.cache[key]=new_node
            self.min_freq=1  
            
            if 1 not in self.freq_map:
                self.freq_map[1]=DoublyLinkedList()
            self.freq_map[1].add_to_head(new_node)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)