class Stack:
    def __init__(self):
        self.items = []  

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  
        return None 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        return None

    def is_empty(self):
        return len(self.items) == 0   
    def size(self):
        return len(self.items)   
    
if __name__ == "__main__":
    s = Stack()
    print("Stack ว่างหรือไม่:", s.is_empty())

    s.push(10)
    s.push(20)
    s.push(30)

    print("ขนาดของ Stack:", s.size())
    print("ค่าบนสุด:", s.peek())
    print("นำออก:", s.pop())
    print("ค่าบนสุดหลัง pop:", s.peek())
    print("Stack ว่างหรือไม่:", s.is_empty())