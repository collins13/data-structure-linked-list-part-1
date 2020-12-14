class Node():
    def __init__(self, data=None):
        self.data = data;
        self.next = None;



class Linked_list:
    def __init__(self):
        self.head = Node();
    

    def append(self, data):
        new_node = Node(data);
        cur = self.head;

        while cur.next !=None:
            cur = cur.next;

        cur.next = new_node;

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


my_list = Linked_list();

# my_list.display();

my_list.append(1);
my_list.append(5);
my_list.append(10);
my_list.length();
# my_list.append(3);
my_list.display();
