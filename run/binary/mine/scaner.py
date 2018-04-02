#!/usr/bin/python

import sys
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
import pprint
    
keyword = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
            'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
            'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
            'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
            'volatile', 'while']

def solve_separate(string, state, fix):
    # this function solve the separate
    # fix the offset
    fix[0] = 1
    return [string, "separate"]

def solve_constant(string, state, fix):
    # solve the constant - string, number
    # number - character - 1
    # char   - character - 0
    # string - character - 0
    if "'" in string or '"' in string:
        fix[0] = 1
    else:
        fix[0] = 1
    return [string, "constant"]

def solve_name(string, state, fix):
    # this function solve the word: name or the keyword
    # need to check and decide whether the name or the keyword
    # keyword - 1, name - 2
    global keyword
    fix[0] = 2
    for i in keyword:
        if i in string:
            return [i, "keyword"]
    return [string, "name"]

def solve_operator(string, state, fix):
    # solve the operator
    if state in [401, 405, 409, 412, 415, 418, 421, 424, 428, 433, 437]:
        fix[0] = 2
    else:
        fix[0] = 1
    return [string, "operator"]

def init_table():
    # this function try to create the defaultdict of the DFA 
    # and return to use

    # main_table save the state and the table or list [process, paramater]
    # table save the character and the state need to change, do not save the function

    main_table      = defaultdict(dict)

    # state 0 
    table           = defaultdict(int)
    table['^[1-9]$']= 1
    table['^0$']    = 8
    table[r'^\'$']  = 12
    table[r'^"$']   = 15
    table['^[a-zA-Z_]$'] = 600
    table[r'^[,;.\(\)\[\]\{\}\s]$'] = 200
    table['^[+]$']  = 400
    table['^[-]$']  = 404
    table['^[*]$']  = 408
    table['^[/]$']  = 411
    table['^[%]$']  = 414
    table['^[=]$']  = 417
    table['^[!]$']  = 420
    table['^[<]$']  = 423
    table['^[>]$']  = 427
    table['^[~]$']  = 431
    table['^[&]$']  = 432
    table['^[|]$']  = 436
    main_table[0]   = table

    # ----------- const (number / string) ----------
    # state 1
    table           = defaultdict(int)
    table['^[0-9]$']= 1
    table[r'^[\.]$'] = 2
    table['^[eE]$'] = 4
    table['^[\s+\-*/%&|?;,]$'] = 7
    main_table[1]   = table

    # state 2
    table           = defaultdict(int)
    table['^[0-9]$']= 3
    main_table[2]   = 3

    # state 3
    table           = defaultdict(int)
    table['^[0-9]$']= 3
    table['^[\s+\-*/%&|?;,]$'] = 7
    table['^[eE]$'] = 4
    main_table[3]   = table

    # state 4
    table           = defaultdict(int)
    table['^[0-9]$']= 6
    table['^[+\-]$']= 5
    main_table[4]   = table

    # state 5
    table           = defaultdict(int)
    table['^[0-9]$']= 6
    main_table[5]   = table

    # state 6
    table           = defaultdict(int)
    table['^[0-9]$']= 6
    table['^[\s+\-*/%&|?;,]$'] = 7
    main_table[6]   = table

    # state 7
    main_table[7]   = [solve_constant, 1]

    # state 8
    table           = defaultdict(int)
    table['^[8-9]$']= 1
    table['^[0-7]$']= 9
    table['^[xX]$'] = 10
    table['^[\s+\-*/%&|?;,]$'] = 7
    main_table[8]   = table

    # state 9
    table           = defaultdict(int)
    table['^[0-7]$']= 9
    table['^[8-9]$']= 1
    table['^[\s+\-*/%&|?;,]$'] = 7
    main_table[9]   = table

    # state 10
    table           = defaultdict(int)
    table['^[0-9a-zA-z]$'] = 11
    main_table[10]  = table

    # state 11
    table           = defaultdict(int)
    table['^[0-9a-zA-Z]$'] = 11
    table['^[\s+\-*/%&|?;,]$'] = 7
    main_table[11]  = table

    # state 12
    table           = defaultdict(int)
    table[r'^[^\\\']$'] = 12
    table[r'^[\\]$']= 13
    table['^[\']$'] = 14
    main_table[12]  = table

    # state 13
    table           = defaultdict(int)
    table['^.$']    = 12
    main_table[13]  = table

    # state 14
    main_table[14]  = [solve_constant, 0]
    
    # state 15
    table           = defaultdict(int)
    table[r'^[^\\\"]$'] = 15
    table[r'^[\\]$']= 16
    table['^[\"]$'] = 17
    main_table[15]  = table

    # state 16
    table           = defaultdict(int)
    table['^.$']    = 15
    main_table[16]  = table

    # state 17
    main_table[17]  = [solve_constant, 0]

    # ---------- separate ----------
    # state 200
    main_table[200] = [solve_separate, None]

    # ---------- name     ----------
    # state 600
    table           = defaultdict(int)
    table['^[0-9a-zA-Z_]$'] = 600
    table['^[\s+\-*/%&|?;,]$'] = 601
    main_table[600] = table

    # state 601
    main_table[601] = [solve_name, None]

    # ---------- operator ----------
    # state 400
    table           = defaultdict(int)
    table['^[^+=]$']= 401
    table['^[+]$']  = 402
    table['^[=]$']  = 403
    main_table[400] = table

    # state 401
    main_table[401] = [solve_operator, None]

    # state 402
    main_table[402] = [solve_operator, None]

    # state 403
    main_table[403] = [solve_operator, None]
    
    # state 404
    table           = defaultdict(int)
    table['^[^-=]$']= 405
    table['^[-]$']  = 406
    table['^[=]$']  = 407
    main_table[404] = table

    # state 405
    main_table[405] = [solve_operator, None]

    # state 406
    main_table[406] = [solve_operator, None]

    # state 407
    main_table[407] = [solve_operator, None]

    # state 408
    table           = defaultdict(int)
    table['^[^=]$'] = 409
    table['^[=]$']  = 410
    main_table[408] = table

    # state 409
    main_table[409] = [solve_operator, None]
    
    # state 410
    main_table[410] = [solve_operator, None]
    
    # state 411
    table           = defaultdict(int)
    table['^[^=]$'] = 412
    table['^[=]$']  = 413
    main_table[411] = table

    # state 412
    main_table[412] = [solve_operator, None]
    
    # state 413
    main_table[413] = [solve_operator, None]
    
    # state 414
    table           = defaultdict(int)
    table['^[^=]$'] = 415
    table['^[=]$']  = 416
    main_table[414] = table

    # state 415
    main_table[415] = [solve_operator, None]
    
    # state 416
    main_table[416] = [solve_operator, None]
    
    # state 417
    table           = defaultdict(int)
    table['^[^=]$'] = 418
    table['^[=]$']  = 419
    main_table[417] = table

    # state 418
    main_table[418] = [solve_operator, None]
    
    # state 419
    main_table[419] = [solve_operator, None]

    # state 420
    table           = defaultdict(int)
    table['^[^=]$'] = 421
    table['^[=]$']  = 422
    main_table[420] = table

    # state 421
    main_table[421] = [solve_operator, None]
    
    # state 422
    main_table[422] = [solve_operator, None]
    
    # state 423
    table           = defaultdict(int)
    table['^[^<=]$']= 424
    table['^[<]$']  = 425
    table['^[=]$']  = 426
    main_table[423] = table

    # state 424
    main_table[424] = [solve_operator, None]

    # state 425
    main_table[425] = [solve_operator, None]

    # state 426
    main_table[403] = [solve_operator, None]
    
    # state 427
    table           = defaultdict(int)
    table['^[^>=]$']= 428
    table['^[>]$']  = 429
    table['^[=]$']  = 430
    main_table[427] = table

    # state 428
    main_table[428] = [solve_operator, None]

    # state 429
    main_table[429] = [solve_operator, None]

    # state 430
    main_table[430] = [solve_operator, None]

    # state 431
    main_table[431] = [solve_operator, None]
    
    # state 432
    table           = defaultdict(int)
    table['^[^&=]$']= 433
    table['^[&]$']  = 434
    table['^[=]$']  = 435
    main_table[432] = table

    # state 433
    main_table[433] = [solve_operator, None]

    # state 434
    main_table[434] = [solve_operator, None]

    # state 435
    main_table[435] = [solve_operator, None]
    
    # state 436
    table           = defaultdict(int)
    table['^[^|=]$']= 437
    table['^[|]$']  = 438
    table['^[=]$']  = 439
    main_table[436] = table

    # state 438
    main_table[438] = [solve_operator, None]

    # state 439
    main_table[439] = [solve_operator, None]

    # state 440
    main_table[440] = [solve_operator, None]

    return main_table

def run(filename, main_table, keyword):
    # read the file
    # run the main algorithm

    # init the register
    char_register   = None
    state_register  = 0
    string_register = ''

    # the begin and the end is for the string_register
    begin = 0
    end   = 0

    # counter
    count = 0

    with open(filename, 'r') as f:
        data   = f.read()
        length = len(data)
        while end < length:
            char_register = data[end]
            end += 1
            # renew the string_register
            string_register += char_register
            if isinstance(main_table[state_register], defaultdict):
                # the middle 
                for i in main_table[state_register]:
                    check = re.compile(i)
                    if check.findall(char_register):
                        # find the row in the sub table
                        state_register   = main_table[state_register][i]
                        break
                else:
                    # wrong case
                    print("Scaner find the wrong in the file,", \
                            string_register, char_register)
            else:
                # end process
                # only in this case, change the begin
                # back to one character age

                # how many character need to go back
                fix = [0]
                res = main_table[state_register][0](string_register, state_register, fix)

                # go back, untread
                string_register = string_register[0:-fix[0]]
                res[0] = string_register

                end -= fix[0]

                if res[0].strip():
                    count += 1
                    print(count, '\t', res[0], '\t', res[1])
                state_register = 0
                char_register  = None
                string_register = ''
                begin = end

if __name__ == "__main__":
    main_table = init_table()
    # sys/argv[1]
    run("../../test.pp.c", main_table, keyword)
