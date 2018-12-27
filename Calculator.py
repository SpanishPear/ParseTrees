#basic calculator parse tree

class ParseTree:
    def __init__(self, tokens):
        pass
    def __str__(self):
        pass
    def evaluate(self):
        pass
    
#note this will not work as it is left recursive
    
class Expression(ParseTree):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.left = Expression(tokens)
        #if there are tokens, and the first token is a plus or minus operand
        if tokens and tokens[0] in ("+", "-"):
            #the operand is the first token
            self.op = tokens[0]
            #token consumed
            del tokens[0]
            self.right = Term(tokens)

        else:
            self.right = None

        def __str__(self):
            if self.right is None:
                return "Expr({})".format(self.left)
            return "expr({} {} {})".format(self.left, self.op,self.right)

        def evaluate(self):
            if self.right is None:
                return self.left.evaluate()
            if self.op == "+":
                return self.left.evaluate() + self.right.evaluate()
            else:
                return self.left.evaluate() -self.right.evaluate()
            
        
