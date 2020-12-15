
            prev = temp;
            temp = prev.next
        if temp == None:
            return
    
        prev.next = temp.next
        temp = None
        