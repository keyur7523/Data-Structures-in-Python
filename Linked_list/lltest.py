class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return "{self.data} . {self.next}"

class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            current = self.head
            while current.next is not None:
                current = current.next 
            current.next = Node(data, None)
            
    def insert_at_start_single_element(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            self.head = Node(data, self.head)
            
    def insert_at_start(self, data_list):
        if self.head is None:
           for i in data_list:
               self.insert_at_end(i)
        else:
            for i in data_list[::-1]:
                self.insert_at_start_single_element(i)
    
    def insert_at_position(self, data, position):
        if position < 1 or position > self.length() + 1:
            raise Exception("Invalid position")
        
        else:
            if position == 1:
                self.insert_at_start_single_element(data)
            elif position == self.length() + 1:
                self.insert_at_end(data)
            else:
                current = self.head
                count = 1
                while count < position:
                    if count == position - 1:
                        new_node = Node(data, current.next)
                        current.next = new_node
                        break
                    count += 1
                    current = current.next
    
    def addAtIndex(self, val, index):
        # 1 -> 2 -> 3 -> 4 -> 5
        # 0.   1.   2.   3.   4.
        ind, curr = 0, self.head
        if index > self.length():
            raise Exception("Index out of range.")
        else:
            if index == 0:
                new_node = Node(val, curr)
                self.head = new_node
            else:
                while ind < index-1:
                    curr = curr.next
                    ind += 1
                new_node = Node(val, curr.next)
                curr.next = new_node
                
    ###  1 -> 2 -> 3 -> 4 -----> 100 -------> 5 -> 6 -> 7 -> 8
    # before adding new element
    # head = 1
    # current = 1
    # count = 1
   
    def remove_nth_element(self, n):
        
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
        
        if self.head is None or n > self.length():
            raise Exception("Out of Index Error.")
        else:
            current = self.head
            count = 1
            if n == 1:
                self.head = current.next
            else:
                count = 1
                next_node = current.next
                while next_node is not None:
                    if count == n-1:
                        if n == self.length():
                            current.next = None
                        else:    
                            current.next = next_node.next
                        break
                        
                    current = next_node
                    next_node = next_node.next 
                    count += 1
                    
    def frequenciesOfElements(self):
        d = {}
        curr = self.head
        while curr.next:
            if curr.data in d.keys():
                d[curr.data] += 1
            else:
                d[curr.data] = 1
            curr = curr.next
        
        if curr.data in d.keys():
            d[curr.data] += 1
        else:
            d[curr.data] = 1

        curr2 = None

        for i in d.values():
            curr2 = Node(i, curr2)
            head2 = curr2

        self.head = head2
                    
    def length(self):
        if self.head is None:
            return 0
        else:
            length, current = 0, self.head
            while current is not None:
                length += 1
                current = current.next
            return length
            
    def __str__(self):
        if self.head == None:
            return "Linked List is empty."
        else:
            string = ""
            current = self.head
            string += str(current.data)
            while current.next is not None:
                string += " -> "
                current = current.next
                string += str(current.data)
            return string
        
    def numComponents(self, nums):
        d = []
        curr = self.head
        while curr.next is not None:
            if curr.data in nums:
                d.append([curr.data])
                break
            curr = curr.next
        while curr.next is not None:
            flag = 0
            if curr.next.data in nums:
                for i in d:
                    if curr.data in i:
                        i.append(curr.next.data)
                        flag = 1
                if not flag:
                    d.append([curr.next.data])
            curr = curr.next
       
        return len(d)
    
    def plusOne(self):

        # 1 -> 2 -> 3

        curr = self.head
        s = ''
        while curr.next is not None:
            s += str(curr.data)
            curr = curr.next
        s += str(curr.data)
        p = int(s)
        p += 1
        print(p)
        
        for i in str(p):
            self.insert_at_end(int(i))
            
    def isPalindrome(self):
        #code here
        # 1 -> 2 -> 3 -> 4
        s = ""
        curr = self.head
        while curr.next:
            s += str(curr.data)
            curr = curr.next
            
        s += str(curr.data)
            
        if s == s[::-1]:
            return 1
        
        return 0
        

if __name__ == "__main__":
    l1 = linkedlist()
    l1.insert_values([1, 2, 1])
    print(l1.isPalindrome())
    
    #l1.insert_at_start_single_element(100)
    # 1 -> 2 -> 3 -> 4
    #l1.insert_at_start([101, 102, 103, 104,105])
    
    # l1.remove_nth_element(1)
    
    print(l1)
    #print(l1.length())