
def isfloat(string):
    array = string.split('.')
    i = 0    
    while  i < len(array) and array[i].isnumeric():
        i = i + 1        
    return i < len(array) or array[i].isnumeric()        
        

class Arbol:
    root = None
    left = None
    right = None

    def __init__(self):
        pass
    
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

    def __init__(self):
        pass
        
    def addToTree(self, symbol):
        if isfloat(symbol):
            if self.left == None:
                self.left = symbol
            elif self.right = None:
                self.right = symbol
            else:
                self.right.addToTree(symbol)
        elif symbol in ('+','-','*','/','%'):
            if (self.root == None):
                self.root = symbol
            elif not self.right == None:
                self.right.addToTree(symbol)
            else:
                self.right = Arbol(symbol)
        else:
             print('no es posible computar el input')

def getInput(tree, string):
    array = string.split()
    for i in range(len(array)):
        tree.addToTree(array[i])

def recorrer(tree):
    if(type(tree.right) == 'Arbol'):
        return recorrer(tree.right)
    else:       
        fRight = float(tree.right)
        fLeft = float(tree.left)
        if tree.root == '+':
            return fRight + fLeft
        elif tree.root == '-':
            return fRight - fLeft
        elif tree.root == '*':
            return fRight * fLeft
        elif tree.root == '/':
            return fRight / fLeft
        elif tree.root == '%':
            return fRight % fLeft    
        
cadena = input()
arbol = Arbol(None)
getInput(arbol, cadena)
recorrer(arbol)
