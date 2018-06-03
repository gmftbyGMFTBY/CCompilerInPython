#!/bin/python
# Author: GMFTBY
# Time  : 2018.6.4

'''
The algorithm is that for every node in the tree,
try to define a return mode, and the root's return 
value is the 4-tuple which we want.
'''

from lxml import etree
import xml.etree.ElementTree as ET
from collections import deque
import pydot, pprint

memoryzone = dict()
parazone   = list(range(100))
pausezone  = list(range(100))

# finally, xmlobj must be the root of the xml tree
def program_return(xmlobj):
    return cmpl_unit_return(xmlobj.getchildren()[0])

# cmpl unit return mode function
def cmpl_unit_return(xmlobj):
    return func_list_return(xmlobj.getchildren()[0])

# func list return mode function
def func_list_return(xmlobj):
    stmt = []
    for child in xmlobj.getchildren():
        if child.tag == "FUNC_DEF": stmt.extend(func_def_return(child))
        else:
            print("something wrong in func define return mode function,", child.tag)
            exit(1)
    return stmt

# func define return mode function
def func_def_return(xmlobj):
    # whether expand the parament getting stmt ?
    children = xmlobj.getchildren()
    stmt, collections = [], dict()
    for child in children:
        if child.tag == "TYPE_SPEC": collections['TYPE_SPEC'] = type_spec_return(child)
        elif child.tag == "separate" or child.tag == "operator": pass
        elif child.tag == "identifier": collections['identifier'] = identifier_return(child)
        elif child.tag == "ARG_LIST": collections['arg_list'] = arg_list_return(child)
        elif child.tag == "CODE_BLOCK": collections['CODE_BLOCK'] = code_block_return(child)
        else:
            print("something wrong in func define return mode function,", child.tag)
            exit(1)
    stmt.append(['F', '_', '_', collections['identifier']])
    stmt.extend(collections['CODE_BLOCK'])
    return stmt

# code block return mode function
def code_block_return(xmlobj):
    children = xmlobj.getchildren()
    return stmt_list_return(children[1])

# stmt list return mode function
def stmt_list_return(xmlobj):
    children = xmlobj.getchildren()
    stmt = []
    for child in children:
        if child.tag == "separate": pass
        elif child.tag == "INIT_STMT": stmt.extend(init_stmt_return(child))
        elif child.tag == "ASSIGN_STMT": stmt.extend(assign_stmt_return(child))
        elif child.tag == "RTN_STMT": stmt.extend(rtn_stmt_return(child))
        else:
            print("something wrong in stmt list return mode function,", child.tag)
            exit(1)
    return stmt

# return stmt return mode function
def rtn_stmt_return(xmlobj):
    # put the return value into the parazone, parazone0 - number of the parament, 1, 2, 3, ...
    # return 1 parament, for easy C comiler building
    children = xmlobj.getchildren()
    result, substmt = expr_return(children[1])
    substmt.append(['=', '1', '_', 'parazone0'])
    substmt.append(['=', result, '_', 'parazone1'])
    return substmt

# assign stmt return mode function
def assign_stmt_return(xmlobj):
    children = xmlobj.getchildren()
    collections = dict()
    for child in children:
        if child.tag == "operator": collections['operator'] = child.text
        elif child.tag == "identifier": collections['identifier'] = child.text
        elif child.tag == "EXPR": collections['EXPR'] = expr_return(child)
        else:
            print('something wrong in assign stmt return mode function,', child.tag)
            exit(1)
    
    result, substmt = collections['EXPR']
    substmt.append(['=', result, '_', collections['identifier']])
    
    return substmt

def parg_return(xmlobj):
    # return the parament in the pausezone
    children = xmlobj.getchildren()
    return expr_return(children[0])

# parg list stmt return mode function
def parg_list_return(xmlobj):
    # return the list of the parament
    # 0 - number of the parament, 1 - paramter 1, 2 - parmter 2, ...
    # the parament save in the parament_zone and can be expend in the data sector
    
    stmt = []
    # get the number of the PARG
    children = xmlobj.getchildren()
    pargs = [i for i in children if i.tag == "PARG"]
    count = len(pargs)
    stmt.append(['=', str(count), '_', 'parazone0'])
    
    # the parament getting
    for index, parg in enumerate(pargs):
        result, substmt = parg_return(parg)
        stmt.extend(substmt)
        stmt.append(['=', result, '_', 'parazone' + str(index + 1)])        # + 1 because the parament begin from 1
    
    return stmt

# call stmt return mode function
def call_stmt_return(xmlobj):
    collections = dict()
    children = xmlobj.getchildren()
    # analyse the call stmt
    for child in children:
        if child.tag == "identifier": collections['identifier'] = identifier_return(child)
        elif child.tag == "operator": collections['operator'] = operator_return(child)
        elif child.tag == "PARG_LIST": collections[child.tag] = parg_list_return(child)
        elif child.tag == "separate": pass
        else:
            print("something wrong in call stmt function,", child.tag)
            exit(1)
    
    stmt = collections['PARG_LIST']
    stmt.append(['C', '_', '_', collections['identifier']])
    return stmt

# expr return mode function
def expr_return(xmlobj):
    # reverse bolan expr to write
    
    # init the pausezone for the expr using
    global pausezone
    pausezone = [0] * 100
    
    funclisthead, funclist, stmt, equ = 0, [], [], []
    for children in xmlobj.iter():
        if children.tag == "CALL_STMT": funclist.append(children)
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
                substmt = call_stmt_return(funclist[funclisthead])
                funclisthead += 1
                stmt.extend(substmt)
                stmt.append(['=', 'parazone0', '_', 'pausezone' + str(pausezone.index(0))])
                equp[-1] = "pausezone" + str(pausezone.index(0))
                pausezone[pausezone.index(0)] = 1
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
    # return the result and the asm stmt
    # print(sym)
    
    first = sym.pop()
    stmt.append(['=', str(first), '_', 'pausezone' + str(pausezone.index(0))])
    sym.append('pausezone' + str(pausezone.index(0)))
    pausezone[pausezone.index(0)] = 1
    operatorstack = []
    while len(sym) != 0:
        operatorstack.append(sym.pop())
        if operatorstack[-1] in '+-*/%':
            op = operatorstack.pop()
            b = operatorstack.pop()
            a = operatorstack.pop()
            if not a.startswith('pausezone'):
                index = 'pausezone' + str(pausezone.index(0))
                stmt.append(['=', str(a), '_', index])
                pausezone[pausezone.index(0)] = 1
                stmt.append([op, index, b, index])
                operatorstack.append(index)
                continue
            stmt.append([op, a, b, a])
            operatorstack.append(a)
            
    if len(operatorstack) != 1:
        print('something wrong in expr return mode function')
        exit(1)
    else:
        return operatorstack[0], stmt

# init stmt return mode function
def init_stmt_return(xmlobj):
    global pausezone    # do not init the pausezone
    collection = dict()
    children = xmlobj.getchildren()
    for child in children:
        if child.tag == "identifier": collection[child.tag] = identifier_return(child)
        elif child.tag == "TYPE_SPEC": collection[child.tag] = type_spec_return(child)
        elif child.tag == "operator": collection[child.tag] = operator_return(child)
        elif child.tag == "EXPR": collection[child.tag] = expr_return(child)
        else:
            print("something wrong in init_stmt_return function,", child.tag)
            exit(1)
    if not collection.get('EXPR'): return [['D', '_', '_', collection['identifier']]]
    else: 
        # init stmt exist the expr consit
        result, substmt = collection.get('EXPR')
        substmt.append(['D', '_', '_', collection['identifier']])
        substmt.append(['=', result, '_', collection['identifier']])    # move the data from the pausezoen to the memory, to save it
        return substmt

# the return mode funciton of the easy or leaf node
# -----------------------------------------
def factor_return(xmlobj):
    # return stmt or factor
    children = xmlobj.getchildren()
    if children[0].tag == "identifier": return identifier_return(children[0])
    elif children[0].tag == "constant": return const_return(children[0])
    elif children[0].tag == "CALL_STMT": return call_stmt_return(children[0])
    elif children[0].tag == "operator": 
        return expr_stmt_return(children[1])
    else:
        print("something wrong in factor_return,", xmlobj.tag)
        exit(1)
    
def type_spec_return(xmlobj):
    return keyword_return(xmlobj.getchildren()[0])

def operator_return(xmlobj):
    return xmlobj.text

def const_return(xmlobj):
    return xmlobj.text

def identifier_return(xmlobj):
    return xmlobj.text

def keyword_return(xmlobj):
    return xmlobj.text

def argument_return(xmlobj):
    type_spec, identifier = xmlobj.getchildren()
    return type_spec_return(type_spec), identifier_return(identifier)

def arg_list_return(xmlobj):
    children = xmlobj.getchildren()
    collections = []
    for child in children:
        if child.tag == "separate": pass
        elif child.tag == "ARGUMENT": collections.append(argument_return(child))
        else:
            print("something wrong in arg list return mode function,", child.tag)
            exit(1)
    return collections

# the utily function for the code
# -----------------------------------------

def showtree(filein, fileout):
    # convert the xmlobj to the photo
    # this is the utilies function we need.
    root = etree.parse(filein).getroot()
    graph = pydot.Dot(graph_type = "digraph")

    # bfs
    head, tail = 0, 1
    noderoot = pydot.Node(root.tag, shape="box", label=root.tag)
    nodestack = deque([(root, noderoot, 1)])
    graph.add_node(noderoot)

    while head < tail:
        children = nodestack[head][0].getchildren()
        for index, child in enumerate(children):
            # balance the tree
            if child.tag == nodestack[head][0].tag: node = nodestack[head][1]
            else: 
                node = pydot.Node(child.tag + str(nodestack[head][2] + 1)\
                    + str(index) + str(head), shape="box", label=child.tag)
                graph.add_node(node)
                graph.add_edge(pydot.Edge(nodestack[head][1], node))
            nodestack.append((child, node, nodestack[head][2] + 1))
        head, tail = head + 1, tail + len(children)

    graph.write_png(fileout)
    
def balance_tree(filein, fileout):
    # read the xml tree of the code (filein), then balance it and write into the fileout
    root = etree.parse(filein).getroot()
    head, tail = 0, 1
    nodestack = deque([root])
    docstack  = deque([etree.Element('PROGRAM')])
    
    while head < tail:
        children = nodestack[head].getchildren()
        for index, child in enumerate(children):
            if child.tag == nodestack[head].tag: docstack.append(docstack[head])
            else: 
                docnode = etree.SubElement(docstack[head], child.tag)
                if child.text: docnode.text = child.text
                else: docnode.text = '\n'
                docstack.append(docnode)
            nodestack.append(child)
        head, tail = head + 1, tail + len(children)
    
    with open(fileout, 'w') as f:
        proot = docstack[0]
        proot.set('name', fileout)
        res = ET.tostring(proot)
        f.write(etree.tostring(etree.fromstring(res), pretty_print=True).decode())
        
# expand the 4-tuple into the X86 asm
# -----------------------------------------
def expand_4_tuple(code):
    # write data segment
    print("DATA    SEGMENT")
    
    print("DATA    ENDS")

if __name__ == "__main__":
    # balance_tree("./test.parser.xml", "./test.balance.xml")
    # showtree("./test.balance.xml", "./test.balance.png")
    
    # 4-tuple
    code = program_return(etree.parse("./test.xml").getroot())
    expand_4_tuple(code)
