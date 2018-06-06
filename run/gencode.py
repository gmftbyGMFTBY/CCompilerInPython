#!/usr/bin/python3
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
import pydot, pprint, sys

memoryzone = dict()
parazone   = list(range(10))
pausezone  = list(range(10))
if_stmt_counter = 0     # save the counter index for the global if_stmt
fout = open(sys.argv[2], 'w')

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
    global memoryzone
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
    result = ['F']
    args = [i[1] for i in collections['arg_list']]
    result.extend(args)
    result.append(collections['identifier'])
    
    stmt.append(result)
    # get the value of the parazone to args
    for index, arg in enumerate(args):
        stmt.append(['=', 'parazone' + str(index + 1), '_', arg])
        # if do not exist in the memory, add it into memory
        if not memoryzone.get(arg): 
            memoryzone[arg] = 1
            stmt.append(['D', '_', '_', arg])
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
        elif child.tag == "IF_STMT": stmt.extend(if_stmt_return(child))
        elif child.tag == "ITER_STMT": 
            if child.getchildren()[0].text == "while":
                stmt.extend(while_iter_stmt_return(child))
            else: stmt.extend(for_iter_stmt_return(child))
        else:
            print("something wrong in stmt list return mode function,", child.tag)
            exit(1)
    return stmt

# for iter stmt return mode function
def for_iter_stmt_return(xmlobj):
    global if_stmt_counter
    state, collections, stmt = 1, dict(), []
    for child in xmlobj.getchildren():
        if child.tag == "operator" or child.tag == "keyword" or child.tag == "separate": pass
        elif child.tag == "STMT": 
            collections[f'STMT{state}'] = stmt_return(child)
            state += 1
        elif child.tag == "CODE_BLOCK": 
            collections[f'CODE_BLOCK'] = code_block_return(child)
        else:
            print("something wrong in for iter stmt return mode function,", child.tag)
            exit(1)
            
    stmt.extend(collections['STMT1'][1])    # must be init stmt
    stmt.append(['L', '_', '_', f'LL1{if_stmt_counter}'])
    stmt.extend(collections['STMT2'][1])
    if stmt[-1][0] == '>':
        # just stmt mode
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JA', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    elif stmt[-1][0] == '<':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JB', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    elif stmt[-1][0] == '>=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNB', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    elif stmt[-1][0] == '<=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNA', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    elif stmt[-1][0] == '==':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JZ', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    elif stmt[-1][0] == '!=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNZ', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    else:
        # expr stmt
        stmt.append(['CMP', '0', collections['just'][0], '_'])
        stmt.append(['JNZ', '_', '_', f'LL2{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'LL3{if_stmt_counter}'])
    
    stmt.append(['L', '_', '_', f'LL4{if_stmt_counter}'])
    stmt.extend(collections['STMT3'][1])
    stmt.append(['JMP', '_', '_', f'LL1{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'LL2{if_stmt_counter}'])
    stmt.extend(collections['CODE_BLOCK'])
    stmt.append(['JMP', '_', '_', f'LL4{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'LL3{if_stmt_counter}'])
    if_stmt_counter += 1
    return stmt

# while iter stmt return mode function
def while_iter_stmt_return(xmlobj):
    # write the while ( stmt ) code_block just for the test, for and other 
    # can be expand easily from this function
    global if_stmt_counter
    stmt, collections = [], dict()
    for child in xmlobj.getchildren():
        if child.tag == "keyword" or child.tag == "operator":
            collections[child.tag] = child.text
        elif child.tag == "STMT": collections['just'] = stmt_return(child)
        elif child.tag == "CODE_BLOCK": 
            collections['CODE_BLOCK'] = code_block_return(child)
        else:
            print("something wrong in iter stmt return mode function,", child.tag)
            exit(1)
    # analyse
    stmt.append(['L', '_', '_', f'EBEGIN{if_stmt_counter}'])
    stmt.extend(collections['just'][1])
    if stmt[-1][0] == '>':
        # just stmt mode
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JA', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '<':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JB', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '>=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNB', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '<=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNA', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '==':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '!=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    else:
        # expr stmt
        stmt.append(['CMP', '0', collections['just'][0], '_'])
        stmt.append(['JNZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'ETRUE{if_stmt_counter}'])
    stmt.extend(collections['CODE_BLOCK'])
    stmt.append(['JMP', '_', '_', f'EBEGIN{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'EFALSE{if_stmt_counter}'])
    if_stmt_counter += 1
    return stmt

# if stmt return mode function
def if_stmt_return(xmlobj):
    # write the if ( stmt ) code_block else code_block for the test
    global if_stmt_counter
    children = xmlobj.getchildren()
    stmt, state, collections = [], 1, dict()
    for child in children:
        if child.tag == "keyword" or child.tag == "operator": pass
        elif child.tag == "STMT": 
            # the stmt always the just_stmt of expr
            collections['just'] = stmt_return(child)
            if collections['just'][0] in [1, 2, 3, 4]:
                print("something wrong in if stmt function,", child.tag, result)
                exit(1)
        elif child.tag == "CODE_BLOCK" and state == 1:
            # if code
            state = 2
            collections['CODE_BLOCK1'] = code_block_return(child)
        elif child.tag == "CODE_BLOCK" and state == 2:
            # else code
            collections['CODE_BLOCK2'] = code_block_return(child)
    # analyse
    stmt.extend(collections['just'][1])
    if stmt[-1][0] == '>':
        # just stmt mode
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JA', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '<':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JB', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '>=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNB', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '<=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNA', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '==':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    elif stmt[-1][0] == '!=':
        stmt[-1] = ['CMP', stmt[-1][1], stmt[-1][2], '_']
        stmt.append(['JNZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    else:
        # expr stmt
        stmt.append(['CMP', '0', collections['just'][0], '_'])
        stmt.append(['JNZ', '_', '_', f'ETRUE{if_stmt_counter}'])
        stmt.append(['JMP', '_', '_', f'EFALSE{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'ETRUE{if_stmt_counter}'])
    stmt.extend(collections['CODE_BLOCK1'])
    stmt.append(['JMP', '_', '_', f'ENEXT{if_stmt_counter}'])
    stmt.append(['L', '_', '_', f'EFALSE{if_stmt_counter}'])
    stmt.extend(collections['CODE_BLOCK2'])
    stmt.append(['L', '_', '_', f'ENEXT{if_stmt_counter}'])
    if_stmt_counter += 1
    return stmt
        
# stmt return mode function, which is also very important in the file
def stmt_return(xmlobj):
    # return 1: the result of the stmt, this set because the expr can be return, separate the different mode of the return value
    # return 2: the stmt in 4-tuple model
    for child in xmlobj.getchildren():
        if child.tag == "RTN_STMT": return 1, rtn_stmt_return(child)
        elif child.tag == "ASSIGN_STMT": return 2, assign_stmt_return(child)
        elif child.tag == "INIT_STMT": return 3, init_stmt_return(child)
        elif child.tag == "IF_STMT": return 4, if_stmt_return(child)
        elif child.tag == "JUST_STMT": return "parazone1", just_stmt_return(child)
        elif child.tag == "EXPR": return expr_return(child)
        else:
            print("something wrong in stmt return mode function,", child.tag)
            exit(1)
            
# just stmt mode function, the pause value move to the para1, 2
def just_stmt_return(xmlobj):
    # ==, parazone1, parazone2, parazone1
    stmt, expr1, expr2, operator = [], None, None, None
    state = 1
    for child in xmlobj.getchildren():
        if child.tag == "operator": operator = child.text
        elif child.tag == "EXPR" and state == 1: 
            expr1 = expr_return(child)
            state = 2
        elif child.tag == "EXPR" and state == 2: expr2 = expr_return(child)
    stmt.extend(expr1[1])
    stmt.append(['=', expr1[0], '_', 'parazone1'])
    stmt.extend(expr2[1])
    stmt.append(['=', expr2[0], '_', 'parazone2'])
    stmt.append([operator, 'parazone1', 'parazone2', 'parazone1'])
    return stmt

# return stmt return mode function
def rtn_stmt_return(xmlobj):
    # put the return value into the parazone, parazone0 - number of the parament, 1, 2, 3, ...
    # return 1 parament, for easy C comiler building
    children = xmlobj.getchildren()
    result, substmt = expr_return(children[1])
    substmt.append(['=', '1', '_', 'parazone0'])
    substmt.append(['=', result, '_', 'parazone1'])
    substmt.append(['R', '_', '_', '_'])    # back to the OSc
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
                stmt.append(['=', 'parazone1', '_', 'pausezone' + str(pausezone.index(0))])
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
    global memoryzone
    # AX, BX, CX, DX, 4 register
    AX, BX, CX, DX = None, None, None, None
    
    # write data segment
    print("DATA     SEGMENT", file=fout)
    # write memory sector, scan all the 4-tuple and write the memory
    mset = set()
    for stmt in code:
        if stmt[0] == 'D': mset.add(tuple(stmt))
    for stmt in mset:
        print(f"{stmt[3]}    DB  ?", file=fout)
        memoryzone[stmt[3]] = 1
    # write the pause sector, 10
    for i in range(10):
        print(f"pausezone{i}    DB      ?", file=fout)
    # write the parazone, 10
    for i in range(10):
        print(f"parazone{i}     DB      ?", file=fout)
    print("DATA     ENDS\n", file=fout)  
    # write code segment
    print("CODE     SEGMENT", file=fout)
    state = 0
    head = None
    for stmt in code:
        if stmt[0] == 'F':
            if state == 0: 
                print(f'{stmt[-1].upper()}    PROC    FAR\n\tASSUME  CS:CODE,DS:DATA,ES:NOTHING\n\tPUSH    DS\n\tXOR     AX,AX\n\tPUSH    AX\n\tMOV     AX,DATA\n\tMOV     DS,AX\n', file=fout)
                state = 1
            else: 
                # parament getting
                print(f'{head}    ENDP\n', file=fout)
                print(f'{stmt[-1].upper()}     PROC', file=fout)
                # print(f'\tPUSH     BP')
                # print(f'\tMOV      BP,SP')
                # print(f'')
                # print(f'\tPOP      BP')
            head = stmt[-1].upper()
        elif stmt[0] == 'D': continue
        elif stmt[0] == '=': 
            source, dest = stmt[1], stmt[3]
            if memoryzone.get(source) or source.startswith('parazone') or source.startswith('pausezone'): cs = True
            else: cs = False
            if memoryzone.get(dest) or dest.startswith('parazone') or dest.startswith('pausezone'): cd = True
            else: cd = False
         
            if not cs and cd:
                # mov number into the memory
                print(f"\tMOV      {dest},{source}", file=fout)
            elif (cs and (not cd)) or ((not cs) and (not cd)): 
                print("something wrong with the mov command,", stmt, file=fout)
                exit(1)
            else:
                # both the argument of the mov command is the RAM unit, check the register
                print(f'\tMOV      AL,{source}', file=fout)
                print(f'\tMOV      {dest},AL', file=fout)
        elif stmt[0] == '+':
            # write the real code of the program
            source1, source2, dest = stmt[1], stmt[2], stmt[3]
            if memoryzone.get(source1) or source1.startswith('parazone') or source1.startswith('pausezone'): cs1 = True
            else: cs1 = False
            if memoryzone.get(source2) or source2.startswith('parazone') or source2.startswith('pausezone'): cs2 = True
            else: cs2 = False
            if memoryzone.get(dest) or dest.startswith('parazone') or dest.startswith('pausezone'): cd = True
            else: cd = False
                
            if cs1 and (not cs2):
                # mov number into the memory
                print(f"\tADD      {source1},{source2}", file=fout)
            elif ((not cs1) and cs2) or ((not cs1) and (not cs2)): 
                print("something wrong with the mov command,", stmt, file=fout)
                exit(1)
            else:
                # both the argument of the mov command is the RAM unit, check the register
                print(f'\tMOV      AL,{source1}', file=fout)
                print(f'\tADD      AL,{source2}', file=fout)
                print(f'\tMOV      {dest},AL', file=fout)
        elif stmt[0] == '-':
            # write the real code of the program
            source1, source2, dest = stmt[1], stmt[2], stmt[3]
            if memoryzone.get(source1) or source1.startswith('parazone') or source1.startswith('pausezone'): cs1 = True
            else: cs1 = False
            if memoryzone.get(source2) or source2.startswith('parazone') or source2.startswith('pausezone'): cs2 = True
            else: cs2 = False
            if memoryzone.get(dest) or dest.startswith('parazone') or dest.startswith('pausezone'): cd = True
            else: cd = False
                
            if cs1 and (not cs2):
                # mov number into the memory
                print(f"\tSUB      {source1},{source2}", file=fout)
            elif ((not cs1) and cs2) or ((not cs1) and (not cs2)): 
                print("something wrong with the mov command,", stmt, file=fout)
                exit(1)
            else:
                # both the argument of the mov command is the RAM unit, check the register
                print(f'\tMOV      AL,{source1}', file=fout)
                print(f'\tSUB      AL,{source2}', file=fout)
                print(f'\tMOV      {dest},AL', file=fout)
        elif stmt[0] == '*':
            source1, source2, dest = stmt[1], stmt[2], stmt[3]
            print(f'\tMOV      AL,{source1}', file=fout)
            print(f'\tMOV      BL,{source2}', file=fout)
            print(f'\tMUL      BL', file=fout)
            print(f'\tMOV      {dest}, AL', file=fout)
        elif stmt[0] == '/': pass
        elif stmt[0] == 'C':
            # call function stmt[3], add the label after this code
            # the parament saved in the parament
            count = int(parazone[0])
            
            print(f'\tCALL     {stmt[3].upper()}', file=fout)
        elif stmt[0] == 'R': print(f'\tRET', file=fout)
        elif stmt[0] == 'L': print(f'\t{stmt[3]}:', file=fout)
        elif stmt[0] == 'JMP': print(f'\tJMP    {stmt[3]}', file=fout)
        elif stmt[0] in ['JA', 'JB', 'JNB', 'JNA', 'JZ', 'JNZ']:
            print(f'\t{stmt[0]}    {stmt[3]}', file=fout)
        elif stmt[0] == 'CMP': 
            print(f'\tMOV    AL,{stmt[1]}', file=fout)
            print(f'\tCMP    AL,{stmt[2]}', file=fout)
        else:
            print('something wrong in expand 4-tuple function,', stmt, file=fout)
            exit(1)
    print(f'{head}     ENDP\n', file=fout)
    print('CODE     ENDS\n\t\tEND     MAIN', file=fout)

if __name__ == "__main__":
    balance_tree(sys.argv[1], sys.argv[1])
    # showtree("./test.parser.xml", "./test.balance.png")
    
    # 4-tuple
    code = program_return(etree.parse(sys.argv[1]).getroot())
    # pprint.pprint(code)
    expand_4_tuple(code)
