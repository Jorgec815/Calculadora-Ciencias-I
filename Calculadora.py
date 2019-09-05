
def isfloat(string):
    array = string.split('.')
    i= 0
    isnumber = True
    while not(isnumber) or i<len(array):
        if not(array[i].isnumeric()):
            isnumer = False
        i = i+1
    return isnumber
        

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
        print(symbol)
        if isfloat(symbol):
            if self.left == None:
                self.left = symbol
            elif self.right == None:
                self.right = symbol
            else:
                self.right = Arbol()
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

def getInput(tree,string):
    array = string.split()
    array.reverse()
    for i in range(len(array)):
        tree.addToTree(array[i])

def recorrer(tree):
    if(type(tree.right) == 'Arbol'):
        if(tree.right.root == '+'):
            return tree.left + recorrer(tree.right)
        elif(tree.right.root == '-'):
            return tree.left - recorrer(tree.right)
        elif(tree.right.root == '*'):
            return tree.left * recorrer(tree.right)
        elif(tree.right.root == '/'):
            return tree.left / recorrer(tree.right)
        elif(tree.right.root == '%'):
            return tree.left % recorrer(tree.right)
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
arbol = Arbol()
getInput(arbol, cadena)
recorrer(arbol)
