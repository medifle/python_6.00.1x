### first version is just a binary tree

class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None 
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value

# Depth First binary Search
def DFSBinary(root, fcn, n):
    '''root is the start node of a tree you want to search downward.
    fcn is the function to test if node value is integer n.
    Returns boolean'''
    stack = [root]
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0], n):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False

# Breadth First binary Search
# there are minor differences between BFSBinary and DFSBinary
# the core difference is between queue which is FIFO and stack which is LIFO
def BFSBinary(root, fcn, n):
    '''root is the start node of a tree you want to search downward.
    fcn is the function to test if node value is integer n.
    Returns boolean'''
    queue = [root]
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0], n):
            return True
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                # this is one of what vary from DFSBinary()
                queue.append(temp.getRightBranch())
            if temp.getLeftBranch():
                # this is another of what vary from DFSBinary()
                queue.append(temp.getLeftBranch())
    return False


# DFS version of getting the path to the search goal
def DFSBinaryPath(root, fcn, n):
    '''root is the start node of a tree you want to search downward.
    fcn is the function to test if node value is integer n.
    Returns boolean'''
    stack = [root]
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0], n):
            return tracePath(stack[0])
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False

def tracePath(node):
    if not node.getParent():
        return [node.value]
    else:
        return [node.value] + tracePath(node.getParent())


# DFS version of searching ordered tree
def DFSBinaryOrdered(root, fcn, n, ltfcn):
    '''root is the start node of a tree you want to search downward.
    fcn is the function to test if node value is integer n.
    ltfcn , which means less than function, is used to compare n and current node value.
    Returns boolean'''
    stack = [root]
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0], n):
            return True
        elif ltfcn(stack[0], n):
            temp = stack.pop(0)
            stack.insert(0, temp.getRightBranch())
        else:
            temp = stack.pop(0)
            stack.insert(0, temp.getLeftBranch())
    return False
            
def ltfcn(node, n):
    if node.value < n:
        return True
    else:
        return False


# create a 8 elements of tree
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

# construct tree
# there are (8 - 1) edges(or branches)
# takes (8 - 1) * 2 lines to construct.
n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)

# define fcn
def find(node, n):
    '''n is an integer
    node is an instance of binaryTree class
    Returns boolean, to test if the value of node equals to n'''
    return node.getValue() == n


### second version is a decision tree

# knapsack problem

# make a decision tree
# for efficiency should really generate on the fly, but here will build and then search

def buildDTree(sofar, todo):
    '''building a decision tree(binary). the tree root is sofarNode whose value is sofar.
    sofar: a list of items already included in knapsack
    todo: a list of items that are not in knapsack needs to be decided 
    which item within the list should be included in knapsack
    Returns root node of the tree: sofarNode'''
    # base case
    if len(todo) == 0:
        # notice this is binaryTree(), not buildDTree()
        # return type is node whose value is sofar without any child
        return binaryTree(sofar)
    # recursion block
    else:
        # create current node, which means an instance of the binaryTree class. 
        # the value of sofarnode is the argument sofar
        sofarNode = binaryTree(sofar)
        
        # create left and right children whose type are also node, an instance of binaryTree class
        # building children recursively could easily create two huge trees whose root nodes are withelt and withoutelt respectively
        # withelt would be a node whose value is (sofar + [todo[0]])
        withelt = buildDTree(sofar + [todo[0]], todo[1:])
        # withoutelt would be a node whose value is sofar
        withoutelt = buildDTree(sofar, todo[1:])
        
        # set withelt as a child of sofarNode
        sofarNode.setLeftBranch(withelt)
        # set withoutelt as a child of sofarNode
        sofarNode.setRightBranch(withoutelt)
        
        # return type is node whose value is sofar with two children.
        # notice one of arguments you passed in is sofar, 
        # while buildDTree function return a node whose value is sofar
        return sofarNode

def DFSDTree(root, valueFcn, constraintFcn):
    '''
    GOAL: every node in a tree is a possible knapsack you want.
    Now you want to find the most valuable knapsack. 
    However the weight of the knapsack should be acceptable.
    NOTICE: every node value, which may be accessed by "node.getValue" method, 
    is a knapsack, which contains several items, 
    and each item encompasses two properties: value and weight.
    
    Arguments Instruction:
    root is the start node of a tree you want to search downward.
    valueFcn is the function to get total value of a knapsack. 
    constraintFcn is the function to check if total weight of a knapsack is below certain amount.
    Returns most valuable knapsack(node).
    '''
    