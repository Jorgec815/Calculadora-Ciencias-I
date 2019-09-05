
def isfloat(string):
    array = string.split('.')  
    i = 0
    isnumber = True
    while isnumber and i < len(array):        
        if not array[i].isnumeric():
            isnumber = False
        i = i+1
    return isnumber
        
class Arbol:
    root = None
    left = None
    right = None    
    
    def __init__(self, root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        
    def addToTree(self, symbol):        
        if isfloat(symbol):
            if self.left == None:
                self.left = symbol                
            elif self.right == None:
                self.right = symbol                
            else:                
                self.right.addToTree(symbol)
        elif symbol in ('+','-','*','/','%'):
            if (self.root == None):
                self.root = symbol
            elif (self.right == None):
                self.right = Arbol(symbol)
            else:
                self.right.addToTree(symbol)            
        else:
             print('no es posible computar el input')

def processInput(tree, string):
    array = string.split()
    array.reverse()
    for i in range(len(array)):
        tree.addToTree(array[i])

def recorrer(tree):
    if type(tree.right) is Arbol:         
        if tree.root == '+':
            return float(tree.left) + recorrer(tree.right)
        elif tree.root == '-':            
            return float(tree.left) - recorrer(tree.right)
        elif tree.root == '*':
            return float(tree.left)  * recorrer(tree.right)
        elif tree.root == '/':
            return float(tree.left) / recorrer(tree.right)
        elif tree.root == '%':
            return float(tree.left) % recorrer(tree.right)
    else:       
        if tree.root == '+':
            return float(tree.left) + float(tree.right)
        elif tree.root == '-':
            return float(tree.left) - float(tree.right)
        elif tree.root == '*':
            return float(tree.left) * float(tree.right)
        elif tree.root == '/':
            return float(tree.left) / float(tree.right)
        elif tree.root == '%':
            return float(tree.left) % float(tree.right)        

arbol = Arbol()
processInput(arbol, input())
print(recorrer(arbol))
