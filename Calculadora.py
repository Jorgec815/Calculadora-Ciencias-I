#Determina si el string pasado como parametro corresponde a un numero, para poder distinguir entre variables y operados en el momento de hacer la insercion en el arbol
def isfloat(string):
    array = string.split('.')  
    i = 0
    isnumber = True
    while isnumber and i < len(array):        
        if not array[i].isnumeric():
            isnumber = False
        i = i+1
    return isnumber
        
class Tree:
    root = None
    left = None
    right = None    

    #constructor
    def __init__(self, root = None, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

    #añade un simbolo(variable o operador) al arbol    
    def addToTree(self, symbol):        
        if isfloat(symbol):
            if self.right == None:
                self.right = symbol               
            elif self.left == None:
                self.left = symbol                
            else:                
                self.left.addToTree(symbol)                
        elif symbol in ('+','-','*','/','%'):
            if (self.root == None):
                self.root = symbol                
            elif (self.left == None):
                self.left = Arbol(symbol)                
            else:
                self.left.addToTree(symbol)            
        else:
             print('No es posible computar el input')

#procesa una entrada, es decir, separa los datos ingresados en un arreglo para añadirlos iterativamente al arbol pasado como parametro
def processInput(tree, string):
    array = string.split()
    array.reverse()
    for i in range(len(array)):
        tree.addToTree(array[i])

#recorre un arbol para devolver un resultado
def travelsTree(tree):
    if type(tree.left) is Tree:         
        if tree.root == '+':
            return travelsTree(tree.left) + float(tree.right)
        elif tree.root == '-':            
            return travelsTree(tree.left) - float(tree.right)
        elif tree.root == '*':
            return travelsTree(tree.left) * float(tree.right)
        elif tree.root == '/':
            return travelsTree(tree.left) / float(tree.right)
        elif tree.root == '%':
            return travelsTree(tree.left) % float(tree.right)
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

tree = Tree()
processInput(tree, input("Digita el input\n"))
print(travelsTree(tree))
