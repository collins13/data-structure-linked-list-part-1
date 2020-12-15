class Node():
    def __init__(self, data=None):
        self.data = data;
        self.next = None;



class Linked_list:
    def __init__(self):
        self.head = Node();
    

    def append(self, data):

        cur = self.head;

        while cur.next !=None:
            cur = cur.next;

        cur.next = Node(data);
    

    def deleteNode(self, key):
        temp =  self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None;
                return
        while temp is not None:
            if temp.data == key:
                break;
            prev = temp;
            temp = prev.next
        if temp == None:
            return
    
        prev.next = temp.next
        temp = None
        
    def length(self):
        cur = self.head;
        total = 0;
        while cur.next !=None:
            total += 1;
            cur = cur.next
        return total;
    
    def display(self):
        elems = [];
        cur_node = self.head;
        while cur_node.next !=None:
            cur_node = cur_node.next
            elems.append(cur_node.data);
        print(elems);

    def contains(self, target):
        curr = self.head
        while curr.next != None:
            if(curr.data == target):
                return True;
            curr = curr.next

        return False;


my_list = Linked_list();

# my_list.display();

my_list.append(1);
my_list.append(5);
my_list.append(7);
my_list.length();
print(my_list.contains(5));
print(my_list.contains(1));
print(my_list.contains(7));
print(my_list.contains(12));
my_list.deleteNode(5);
my_list.deleteNode(1);
# my_list.append(3);
my_list.display();
