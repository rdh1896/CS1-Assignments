"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Russell Harvey <rdh1896@rit.edu>
"""

from dataclasses import dataclass


@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: 'MathNode'
    op: str
    right: 'MathNode'


@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str
    
##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    if tokens == []:
        return None
    elif tokens[0].isdigit():
        return LiteralNode(tokens.pop(0))
    elif tokens[0].isidentifier():
        return VariableNode(tokens.pop(0))
    else:
        operator = tokens.pop(0)
        return MathNode(parse(tokens), operator, parse(tokens))
            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if node is None:
        return ""
    elif isinstance(node, VariableNode):
        if node.name.isidentifier():
            return str(node.name)
    elif isinstance(node, LiteralNode):
        if node.val.isdigit():
            return str(node.val)
    elif isinstance(node, MathNode):
        return infix(node.left) + node.op + infix(node.right)
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if node is None:
        return ""
    elif isinstance(node, VariableNode):
        return int(symTbl[node.name])
    elif isinstance(node, LiteralNode):
        return int(node.val)
    elif isinstance(node, MathNode):
        if node.op == "+":
            return (evaluate(node.left, symTbl)) + (evaluate(node.right, symTbl))
        elif node.op == "-":
            return (evaluate(node.left, symTbl)) - (evaluate(node.right, symTbl))
        elif node.op == "*":
            return (evaluate(node.left, symTbl)) * (evaluate(node.right, symTbl))
        elif node.op == "//":
            return (evaluate(node.left, symTbl)) // (evaluate(node.right, symTbl))

##############################################################################
# create_symbols
##############################################################################

def create_symbols(file):
    """
    Creates a symbol table from an file input.
    :param file: Symbol table file
    :return: symbols
    """
    symbols = {}
    with open(file) as file:
        for line in file:
            if line == "":
                break
            lst = line.split()
            symbols[lst[0]] = lst[1]
    return symbols

##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symbols = create_symbols(inFile)
    print("Symbol Table:", symbols)
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        prefix_lst = prefixExp.split()
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        exp_tree = parse(prefix_lst)
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_str = infix(exp_tree)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", infix_str)
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        solution = evaluate(exp_tree, symbols)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", solution)
         
    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()