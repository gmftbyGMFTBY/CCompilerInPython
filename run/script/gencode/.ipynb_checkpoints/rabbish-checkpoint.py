#!/bin/python

# define the table of the program
# [name, type, value]

from lxml import etree

parament_zone = []    # the paramter zone, default is 100 parament for maximun
memory_zone   = dict()              # the memory zone
pause_zone    = []    # the pause zone save the register used in expr
preinclude    = ['INIT_STMT', 'ASSIGN_STMT', 'EXPR', 'JUST_STMT', 'IF_STMT', 'ITER_STMT', 'CALL_STMT']

def call_stmt(xmlobj):
    # solve and return 4-tuple of the call_stmt
    return [], 'lantian'

def expr(xmlobj):
    # reverse bolan expr to write
    stmt = []
    equ = []
    for children in xmlobj.iter():
        text = children.text
        if not text or not text.strip(): continue
        else: equ.append(text)
    
    # reverse bolan expression
    # prepose for the call_stmt
    equp, state, i, length = [], 0, 0, len(equ)
    while True:
        if i == length: break

        if equ[i] not in '+-*/%()': 
            equp.append(equ[i])
            state, i = 1, i + 1
        else:
            if equ[i] == '(' and state == 1:
                # the call stmt
                pause = [equp[-1]]
                while equ[i] != ')':
                    pause.append(equ[i])
                    i += 1
                pause.append(')')
                i += 1
                substmt, result = call_stmt(pause)
                stmt.extend(stmt)
                equp[-1] = result
                state = 0
            else: 
                equp.append(equ[i])
                state, i = 0, i + 1
    
    # reverse polan expr
    sym, ope = [], []
    for label in equp:
        if label not in '+-*/%()': sym.append(label)
        else:
            if len(ope) == 0: ope.append(label)
            elif label in '+-' and ope[-1] in '*/%':
                while not (len(ope) == 0 or ope[-1] in '+-'):
                    sym.append(ope.pop())
                ope.append(label)
            elif label == ')':
                while ope[-1] != '(':
                    sym.append(ope.pop())
                ope.pop()
            else: ope.append(label)
    
    while len(ope) != 0:
        sym.append(ope.pop())
    
    sym.reverse()

    # create the asm code

    print(sym)
    return [], 1

def assign_stmt(xmlobj):
    # use expr
    stmt = []
    for children in xmlobj.getchildren():
        if children.tag == 'EXPR': 
            substmt, result = expr(children)       # result in memory_zone, stmt is the 4-tuple
            stmt.extend(substmt)
        elif children.tag == 'identifier': name = children.text
    stmt.append(['=', result, '_', name])
    return stmt

def init_stmt(xmlobj):
    # get the xml object, return the 4-tuple of this init stmt
    stmt = []
    result = None
    for children in xmlobj.getchildren():
        if children.tag == "TYPE_SPEC": kind = children.getchildren()[0].text
        elif children.tag == "identifier": name = children.text
        elif children.tag == "EXPR": 
            substmt, result = expr(children)       # result is the expr's name in memory
            stmt.extend(substmt)
        elif children.tag == "operator": pass
        else:
            # operator or error
            print("init wrong", children.tag)
            exit(1)

    # return stmt
    if result:
        memory_zone[name] = (kind, result)
        stmt.append(['D', result, '_', name])
    else:
        memory_zone[name] = (kind, None)
        stmt.append(['D', '_', '_', name])
    return stmt

def analyse_tree(tree):
    # get the tree, and recursively analyse the tree, get the 4-tuple
    for children in tree.getchildren():
        if children.tag in preinclude:
            # find the preinclude, but should remember the NT phenomeno
            if children.tag == "INIT_STMT":
                # The init stmt, add the variable into the memory_zone
                init_stmt(children)
            elif children.tag == "ASSIGN_STMT":
                assign_stmt(children)
            else:
                pass
        else:
            # not the preinclude stmt, try to recursive
            analyse_tree(children)

def main(filename):
    # read the file of the xml tree
    root = etree.parse(filename).getroot().find('CMPL_UNIT')
    analyse_tree(root)

if __name__ == "__main__":
    main("./test.parser.xml")
