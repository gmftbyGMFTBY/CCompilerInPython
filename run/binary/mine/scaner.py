#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

def solve_separate(character):
    # this function solve the separate
    pass

def solve_constant(character):
    # solve the constant - string, number
    # number - character - 1
    # char   - character - '
    # string - character - "
    pass

def solve_word(character=None):
    # this function solve the word: name or the keyword
    # need to check and decide whether the name or the keyword
    pass

def solve_operator(character=None):
    # solve the operator
    pass

def init_table():
    # this function try to create the defaultdict of the DFA 
    # and return to use

    # main_table save the state and the table or list [process, paramater]
    # table save the character and the state need to change, do not save the function

    main_table      = defaultdict(dict)

    # state 0 
    table           = defaultdict(int)
    table['not0']   = 1
    table['0']      = 8
    table["'"]      = 12
    table['"']      = 15
    table['separate'] = 200
    table['char_']  = 600
    main_table[0]   = table

    # state 

    return main_table

def run(filename, table, keyword):
    # read the file
    # run the main algorithm

    # init the register
    char_register   = None
    state_register  = 0
    string_register = ''

    # the begin and the end is for the string_register
    begin = 0
    end   = 0

    # make the character group
    digit     = '0123456789'
    _digit    = 'eE.+-'
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # contain the white space
    separater = [',', ';', ' ', ':', '.', '(', ')', '[', ']', '{', '}']
    operator  = ['+', '++', '+=', '-', '--', '-=', '*', '*=', '/', '/=', '%', '%=', '=', '==', '!', '!=', '<', '<=', '<<', '>', '>=', '>>', '~', '&', '&&', '&=', '|', '||', '|=']
    # the ending charater for number
    other_1   = [' ', '+', '-', '*', '/', '%', '&', '|', '?', ';', ',']
    # the ending charater for name
    other_2   = [' ', '+', '-', '*', '/', '%', '&', '|', '?', ';', ',']
    # the ending charater for operator
    other_3   = []
    # do not need to operate these character
    filte     = ['\n', '\t']

    with open(filename, 'r') as f:
        data = f.read()
        pass



        

if __name__ == "__main__":
    import pprint
    main_table = init_table()
    # pprint.pprint(main_table)

    # 32 keyword in C
    keyword = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
            'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
            'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
            'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
            'volatile', 'while']

    run("../../test.pp.c", main_table, keyword)
