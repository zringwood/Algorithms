import random, time

#Basic Tree Implementation
class Node:
    def __init__(self,value,children) :
        self.value = value
        self.children = children
    def __str__(self) :
        buffer = ""
        for child in self.children:
            buffer += (str)(child.value) + " , "
        return "{} [{}]".format(self.value,buffer)

def printtree(node):
    if len(node.children) == 0:
        print(node)
    print(node)
    for child in node.children :
        printtree(child)

#Build a random tree
size = 10
maxval = 10
root = Node(random.randint(0,maxval),[])
curr = root
queue = [root]
while len(queue) > 0 :
    children = random.randint(1,5)
    size -= children
    if size < 0:
        break;
    for i in range(children):
        child = Node(random.randint(0,maxval),[])
        curr.children.append(child)
        queue.append(child)
    curr = queue.pop(0)

#Breadth first search
def breadthfirstsearch(root, target):
    stack = [root]
    
    while len(stack) > 0 :
        curr = stack.pop(0)
        if curr.value == target :
            return curr
        
        if len(curr.children) > 0:
            stack += curr.children

print(breadthfirstsearch(root, random.randint(0,maxval)))








