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

    main_table = defaultdict(dict)

    # main_table - 0
    table               = defaultdict(int)
    table["\""]         = 10
    table["'"]          = 8
    table["digit"]      = 1
    table[',']          = 12
    table[';']          = 13
    table['white_space']= 14
    table[':']          = 15
    table['.']          = 16
    table['(']          = 17
    table[')']          = 18
    table['[']          = 19
    table[']']          = 20
    table['{']          = 21
    table['}']          = 22
    table['+']          = 23
    table['-']          = 27
    table['*']          = 31
    table['/']          = 34
    table['%']          = 37
    table['=']          = 40
    table['!']          = 43
    main_table[0]       = table

    # main_table - 1
    table               = defaultdict(int)
    table['digit']      = 1
    table['.']          = 2
    table['e/E']        = 4
    table['other_1']    = 7
    main_table[1]       = table

    # main_table - 2
    table               = defaultdict(int)
    table['digit']      = 3
    main_table[2]       = table

    # main_table - 3
    table               = defaultdict(int)
    table['digit']      = 3
    table['e/E']        = 4
    table['other_1']    = 7
    main_table[3]       = table

    # main_table - 4
    table               = defaultdict(int)
    table['+/-']        = 5
    table['digit']      = 6
    main_table[4]       = table

    # main_table - 5
    table               = defaultdict(int)
    table['digit']      = 6
    main_table[5]       = table

    # main_table - 6
    table               = defaultdict(int)
    table['digit']      = 6
    table['other_1']    = 7
    main_table[6]       = table

    # main_table - 7
    main_table[7]       = [solve_constant, 1]

    # main_table - 8
    table               = defaultdict(int)
    table['not \'']     = 8
    table['\'']         = 9
    main_table[8]       = table

    # main_table - 9
    main_table[9]       = [solve_constant, '\'']

    # main_table - 10
    table               = defaultdict(int)
    table['not "']      = 10
    table['"']          = 11
    main_table[10]      = table

    # main_table - 11
    main_table[11]      = [solve_constant, '"']

    # main_table - 12
    main_table[12]      = [solve_separate, ',']
    # main_table - 13
    main_table[13]      = [solve_separate, ';']
    # main_table - 14
    main_table[14]      = [solve_separate, 'white_space']
    # main_table - 15
    main_table[15]      = [solve_separate, ':']
    # main_table - 16
    main_table[16]      = [solve_separate, '.']
    # main_table - 17
    main_table[17]      = [solve_separate, '(']
    # main_table - 18
    main_table[18]      = [solve_separate, ')']
    # main_table - 19
    main_table[19]      = [solve_separate, '[']
    # main_table - 20
    main_table[20]      = [solve_separate, ']']
    # main_table - 21
    main_table[21]      = [solve_separate, '{']
    # main_table - 22
    main_table[22]      = [solve_separate, '}']

    # main_table - 23
    table               = defaultdict(int)
    table['other_3']    = 24
    table['+']          = 25
    table['=']          = 26
    main_table[23]      = table

    # main_table - 24
    main_table[24]      = [solve_operator, None]

    # main_table - 25
    main_table[25]      = [solve_operator, None]

    # main_table - 26
    main_table[26]      = [solve_operator, None]
    
    # main_table - 27
    table               = defaultdict(int)
    table['other_3']    = 28
    table['+']          = 29
    table['=']          = 30
    main_table[27]      = table

    # main_table - 28
    main_table[28]      = [solve_operator, None]

    # main_table - 29
    main_table[29]      = [solve_operator, None]

    # main_table - 30
    main_table[30]      = [solve_operator, None]

    # main_table - 31
    table               = defaultdict(int)
    table['other_3']    = 32
    table['=']          = 33
    main_table[31]      = table

    # main_table - 32
    main_table[32]      = [solve_operator, None]

    # main_table - 33
    main_table[33]      = [solve_operator, None]

    # main_table - 34
    table               = defaultdict(int)
    table['other_3']    = 35
    table['=']          = 36
    main_table[34]      = table

    # main_table - 35
    main_table[35]      = [solve_operator, None]

    # main_table - 36
    main_table[36]      = [solve_operator, None]

    # main_table - 37
    table               = defaultdict(int)
    table['other_3']    = 38
    table['=']          = 39
    main_table[37]      = table

    # main_table - 38
    main_table[38]      = [solve_operator, None]

    # main_table - 39
    main_table[39]      = [solve_operator, None]

    # main_table - 40
    table               = defaultdict(int)
    table['other_3']    = 41
    table['=']          = 42
    main_table[40]      = table

    # main_table - 41
    main_table[41]      = [solve_operator, None]

    # main_table - 42
    main_table[42]      = [solve_operator, None]

    # main_table - 43
    table               = defaultdict(int)
    table['other_3']    = 44
    table['=']          = 45
    main_table[43]      = table

    # main_table - 44
    main_table[44]      = [solve_operator, None]

    # main_table - 45
    main_table[45]      = [solve_operator, None]


    # main_table - 46
    table               = defaultdict(int)
    table['other_3']    = 47
    table['=']          = 48
    table['<']          = 49
    main_table[46]      = table

    # main_table - 47
    main_table[47]      = [solve_operator, None]

    # main_table - 48
    main_table[48]      = [solve_operator, None]

    # main_table - 49
    main_table[49]      = [solve_operator, None]


    # main_table - 50
    table               = defaultdict(int)
    table['other_3']    = 51
    table['=']          = 52
    table['>']          = 53
    main_table[50]      = table

    # main_table - 51
    main_table[51]      = [solve_operator, None]

    # main_table - 52
    main_table[52]      = [solve_operator, None]

    # main_table - 53
    main_table[53]      = [solve_operator, None]

    # main_table - 54
    main_table[54]      = [solve_operator, None]
    
    # main_table - 55
    table               = defaultdict(int)
    table['other_3']    = 56
    table['&']          = 57
    table['=']          = 58
    main_table[55]      = table

    # main_table - 56
    main_table[56]      = [solve_operator, None]

    # main_table - 57
    main_table[57]      = [solve_operator, None]

    # main_table - 58
    main_table[58]      = [solve_operator, None]

    
    # main_table - 59
    table               = defaultdict(int)
    table['other_3']    = 60
    table['|']          = 61
    table['=']          = 62
    main_table[59]      = table

    # main_table - 60
    main_table[60]      = [solve_operator, None]

    # main_table - 61
    main_table[61]      = [solve_operator, None]

    # main_table - 62
    main_table[62]      = [solve_operator, None]

    # main_table - 64
    table               = defaultdict(int)
    table['character,digit,_']=64
    table['other_2']    = 65
    main_table[64]      = table

    # main_table - 65
    main_table[65]      = [solve_word, None]

    return main_table

if __name__ == "__main__":
    import pprint
    main_table = init_table()
    pprint.pprint(main_table)
