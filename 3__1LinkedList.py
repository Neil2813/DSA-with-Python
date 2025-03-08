class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None


class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        self.length = 0

        for value in values:
            self.append(value)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.Value)
            temp = temp.Next

    def append(self, Value):
        new_node = Node(Value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.Next = new_node
            self.tail = new_node
        self.length += 1  # Corrected assignment
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while temp.Next:
            pre = temp
            temp = temp.Next
        self.tail = pre
        self.tail.Next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.Value

    def prepend(self, Value):
        new_node = Node(Value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.Next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.Next
        temp.Next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.Value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.Next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.Value = value
            return True
        return False
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp=prev.Next
            prev.Next=temp.Next 
            temp.Next = None
            self.length -= 1
            return temp
        
    


# Testing
my_linked_list = LinkedList(4, 66, 53)
my_linked_list.append(21)
print('The popped node is', my_linked_list.pop())
my_linked_list.prepend(21)
my_linked_list.pop_first()
print('The popped node is', my_linked_list.pop())
print("The Linked List is: ")
my_linked_list.print_list()
my_linked_list.append(21)
my_linked_list.append(231)
my_linked_list.set_value(1,44)
my_linked_list.print_list()
my_linked_list.remove(1)
print(my_linked_list.get(2).Value)  # Printing the value instead of object
print("The Linked List is: ")
my_linked_list.print_list()




