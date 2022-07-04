
class Stack:
    # Constructor
    def __init__(self):
        self.stack = []
        self.maxSize = 4
        self.top = 0
    # Adds element to the Stack
    def push(self, data):
        if self.top >= self.maxSize:
            print ("Stack Full!")
        else:
            self.stack.append(data)
            self.top += 1
            return True
    # Removes element from the stack
    def pop(self):
        if self.top <= 0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item + " Popped from stack "
    # Return the top element of the stack
    def peek(self):
        if self.top <= 0:
            return ("Stack Empty!")
        else:
            return f"the top element of the stack is {self.stack[-1]}"
    #Return the minimum element in the stack
    def getmin(self) :
        if self.top <= 0:
            return ("Stack Empty!")
        else: 
            # try:
                return f" the minimum element in the stack is {min(int(i) for i in self.stack)}" 
            # except:
            #     raise ValueError("text must be a string")       
    #Check that the stack is empty
    def isEmpty(self):
        return f" Is the stack Empty? {self.stack == []}"
    # Check the fullness of the stack
    def isfull(self):
        return f" Is the stack Full? {self.top == self.maxSize}"
    #Print the values in the stack
    def printStack(self):
        return self.stack
#Driver code
if __name__ == "__main__":
    s = Stack()
    print("***"+" Stack Using Array "+"***")
    while(True):
        el = int(input("1- for Push\n2- or Pop\n3- for peek \n4- to getMin\n5- isEmpty\n6- isfull \n7-showStack \n8- to exit\nselect: "))
        if(el == 1):
            item = input("Enter Element to push in stack\n")
            s.push(item)
            print(item + " pushed to stack ")
        if(el == 2):
            print(s.pop())
        if(el == 3):
            print(s.peek())
        if(el == 4):
            print(s.getmin())
        if(el == 5):
            print(s.isEmpty())
        if(el == 6):
            print(s.isfull())
        if(el == 7):
            print(s.printStack())
        if(el == 8):
            break
