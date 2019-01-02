'''• Two steps:
• Parse the input into something which can be evaluated
• Evaluate the returned object
• Build an object tree while parsing!
• Here’s the grammar we will use in this example:
1 <e1> ::= <e2> ( "+" <e1> )?
2 <e2> ::= <e3> ( "*" <e2> )?
3 <e3> ::= "-"? ( "0" | "1" | ... | "9" )+
4 <e3> ::= "(" <e1> ")"
1,2: <e2> evaluated before <e1>
3,4: <e3> is either an integer or a compound expression'''

#Node Template
class Node:
    def __init__(self, left, right):
        #self.left is the object on the left (in the tree)
        self.left = left
        #self.right is the object on the right (in the tree)
        self.right = right
    def eval(self):
        raise NotImplementedError()
#Subclasses

class AddNode(Node):
    def eval(self):
        #an add node means: left node + right node
        return self.left.eval() + self.right.eval()

class MultNode(Node):
    def eval(self):
        #multiplication node means: left node * right node
        return self.left.eval() * self.right.eval()

class LiteralNode(Node):
    def __init__(self,value):
        #super calls the init function of the superclass, ie the NODE class
        #using None,None as parameters implies no right or left value is needed to parse a literal Node
        super().__init__(None,None)
        #sets "value" of the node to the literal value of the node
        self.value = value
    def eval():
        return self.value

#------------------------PARSER ------------------------
class Parser:
    pass
