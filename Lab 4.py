'''
Andrew Kozempel
CMPSC 413
Lab 4
Fall 2023
'''

import heapq

#### PART 1 - ARRAY ####

class PQ_Array:

    # initialize with is_max flag for sorting
    def __init__(self, is_max=True):
        self.queue = []
        self.is_max = is_max

    # insert/append
    def insert(self, item, priority):
        self.queue.append((item, priority))

        # sort based on min or max
        self.queue.sort(key=lambda x: x[1], reverse=self.is_max)

    # get first element if not empty
    def peek(self):

        if self.queue:
            return self.queue[0]  
        
        else:
            return None

    # delete first element if not empty
    def delete(self):

        if self.queue:
            return self.queue.pop(0)
        
        else:
            return None

    # change elements priority
    def change_priority(self, item, new_priority):

        # for index and tuple pair
        for i, (ele, priority) in enumerate(self.queue):

            # if element is the item
            if ele == item:

                # change elements priority and sort
                self.queue[i] = (item, new_priority)
                self.queue.sort(key=lambda x: x[1], reverse=self.is_max)

#### PART 2 - Linked List ####

# node class for linked list
class Node:

    # initialize node with item, priority
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None

class PQ_LinkedList:

    # initialize empty linked list
    def __init__(self, is_max=True):
        self.head = None
        self.is_max = is_max

    def insert(self, item, priority):

        # create new node based on element and priority
        new_node = Node(item, priority)

        if self.is_max:

            # if LL is empty or new node priority is greater than head's
            if self.head is None or new_node.priority > self.head.priority:

                # insert new node at beginning
                new_node.next = self.head
                self.head = new_node

            # if LL is not empty
            else:

                # current pointer
                current = self.head

                # cycle through elements until 
                # you get to correct priority position
                while current.next is not None and current.next.priority >= new_node.priority:
                    current = current.next

                # add node to position you just determined
                new_node.next = current.next
                current.next = new_node

        else:

            # if LL is empty or new node priority is greater than head's
            if self.head is None or new_node.priority < self.head.priority:

                # insert new node at beginning
                new_node.next = self.head
                self.head = new_node

            # if LL is not empty
            else:

                # current pointer
                current = self.head

                # cycle through elements until 
                # you get to correct priority position
                while current.next is not None and current.next.priority <= new_node.priority:
                    current = current.next

                # add node to position you just determined
                new_node.next = current.next
                current.next = new_node

    def peek(self):

        # if LL not empty, return head values
        if self.head:
            return (self.head.item, self.head.priority)
        else:
            return None
        
    def delete(self):

        # if LL not empty, return head values
        if self.head:

            # store values to return
            item = self.head.item
            priority = self.head.priority

            # make second item the new head
            self.head = self.head.next

            # return values
            return item, priority
        
        else:
            return None

    def change_priority(self, item, new_priority):

        # current pointer
        current = self.head
        previous = None
        
        # cycle through items
        while current:

            # if current item is found
            if current.item == item:

                # if not first item/head
                if previous is not None:

                    # remove/unlink current from LL
                    previous.next = current.next

                # if first item/head
                else:
                    # remove/unlink head/current
                    self.head = current.next    

                # break after removed
                break

            # shift previous and current up
            previous = current
            current = current.next

        if current:

            # update priority and re insert item
            current.priority = new_priority
            self.insert(current.item, current.priority)
        
#### PART 3 - Min/Max Heaps ####

class PQ_MinHeap:

    # intitialize heap as list
    def __init__(self):
        self.heap = []

    # insert using heapq.heappush
    def insert(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    
    def peek(self):
        
        # if heap is not empty
        if self.heap:

            # return item with min priority 
            priority, item = self.heap[0]
            return item, priority
        
        else:
            return None

    def delete(self):

        # if heap is not empty
        if self.heap:

            # delete and return item with min priority 
            priority, item = heapq.heappop(self.heap)
            return item, priority
        
        else:
            return None

    def change_priority(self, item, new_priority):

        # iterate through elements in heap
        for i, (priority, heap_item) in enumerate(self.heap):
            
            # if item is found
            if heap_item == item:

                # set new priority based on index and rearrange
                self.heap[i] = (new_priority, item)
                heapq.heapify(self.heap)
                return

class PQ_MaxHeap:

    # intitialize heap as list
    def __init__(self, is_max=True):
        self.heap = []
        self.is_max = is_max

    # insert using heapq.heappush (negated priority)
    def insert(self, item, priority):
        if self.is_max:
            heapq.heappush(self.heap, (-priority, item))
        else:
            heapq.heappush(self.heap, (priority, item))


    def peek(self):

        if self.is_max:
            # if heap is not empty
            if self.heap:

                # return item with max priority (negate)
                priority, item = self.heap[0]
                return item, -priority
            
        else:
            # if heap is not empty
            if self.heap:

                # return item with min priority 
                priority, item = self.heap[0]
                return item, priority
            
       
        return None

    def delete(self):

        if self.is_max:
            # if heap is not empty
            if self.heap:

                # delete and return item with max priority (negate)
                priority, item = heapq.heappop(self.heap)
                return item, -priority
        
        else:
            # if heap is not empty
            if self.heap:

                # delete and return item with min priority 
                priority, item = heapq.heappop(self.heap)
                return item, priority
        
        return None

    def change_priority(self, item, new_priority):

        if self.is_max:
            # iterate through elements in heap
            for i, (priority, ele) in enumerate(self.heap):

                # if item is found
                if ele == item:

                    # set new priority based on index and rearrange
                    self.heap[i] = (-new_priority, item)
                    heapq.heapify(self.heap)
                    return
        else:    
            # iterate through elements in heap
            for i, (priority, heap_item) in enumerate(self.heap):
                
                # if item is found
                if heap_item == item:

                    # set new priority based on index and rearrange
                    self.heap[i] = (new_priority, item)
                    heapq.heapify(self.heap)
                    return