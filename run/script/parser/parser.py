#!/home/lantian/anaconda3/bin/python
# Author: GMFTBY
# Time  : 2018.4.29

'''
Use LR(1) Algorithm to create the parser of the C language.
As we know, the standard C language is the LR(1) language.

The only constrant of the rule is that the first rule must be the last element
of the whole rules.
'''

import pprint
from show import draw
import sys
import xml.etree.ElementTree as ET
import pickle

class LR:
    def __init__(self, filename, Begin_symbol):
        self.begin_symbol = Begin_symbol

        # read the file of the rules
        with open(filename, 'r') as f:
            # filte the comment of the file `rules`
            self.rules = list(map(lambda line: line[:-1], \
                    filter(lambda line: False if line[:2] == "//" \
                    or not line.strip() else True, f.readlines())))

            # self.rules_bag = self.get_rules_bag()
            for rule in self.rules:
                if rule.split('->')[0].strip() == Begin_symbol:
                    _, right = rule.split('->')
                    right = '·' + right
                    self.BLRP = (Begin_symbol + ' -> ' + right, '#')
                    break
            else:
                print("Can not find", Begin_symbol)
                exit(1)

        # get all character
        self.V_t, self.V_n = self.get_character()

        # get the LR group, GO is a dict saving the transmit information
        # group is the Project group
        self.group, self.GO = self.get_group()

        # init the action and the goto table
        self.action, self.goto = self.init_table()

        # draw the picture, just for debug
        # self.draw()
        # self.read_table()
        print("Init the LR(1) analyser table successfully!")

    def draw(self):
        # use the show.py to draw the picture
        with open('./picture/pic', 'w') as f:
            # write node
            for index, group in enumerate(self.group):
                f.write(f"[node|{index}]: [begin]\n")
                for project in group:
                    f.write(f'{project[0]}, {project[1]}\n')
                f.write('\n')
            # write edge
            for index, item in enumerate(self.GO.items()):
                key, value = item
                f.write(f'[edge|{index}]:\n')
                f.write(f'{key[0]} -> {value} : {key[1]}\n\n')
        draw('./picture/pic')

    def get_character(self):
        V_n = set()
        V   = set()
        for rule in self.rules:
            left, right = rule.split('->')
            V_n.add(left.strip())

            V.add(left.strip())
            for char in right.split():
                V.add(char)
        return V - V_n, V_n
    
    def get_closure(self, begin):
        # get the closure of the LR(1) Project
        bag = set([begin])
        while True:
            size = len(bag)
            for project in list(bag):
                pro = project[0]
                _, right = pro.split('->')
                creators = right.split()
                index = creators.index('·')
                length = len(creators)
                    
                if index + 1 < length: B = creators[index + 1]
                else: B = None
                if index + 2 < length: beta = creators[index + 2:]
                else: beta = None

                if not B:
                    # do not have the B, end get closure
                    continue
                else:
                    if beta: 
                        searcher = set()
                        for ttt in beta:
                            res = self.get_first(ttt)
                            searcher |= res
                            if '@' not in res: break
                        else:
                            searcher |= set([project[1]])

                        searcher -= set(['@'])
                    else:
                        searcher = set([project[1]])
                        
                    for rule in self.rules:
                        if rule.split('->')[0].strip() == B:
                            _, right = rule.split('->')
                            if len(right.split()) == 1 and right.split()[0] == '@': right = '·'
                            else: right = '·' + right
                            for search in searcher:
                                bag.add((B + ' -> ' + right, search))
            if len(bag) == size: break
        # bag is the set of the closure
        return bag

    def goto(self, I, X):
        # the goto function, I - project group, X - the transmit symbol
        J = set()
        for pro, search in I:
            left, right = pro.split('->')
            creators = right.split()
            index = creators.index('·')
            
            if index + 1 < len(creators) and creators[index + 1] == X:
                string = [left.strip(), '->']
                string.extend(creators[:index])
                string.extend([X, '·'])
                if index + 2 < len(creators): string.extend(creators[index + 2:])
                string = ' '.join(string)
                J.add((string, search))
        
        res = set()
        for project in J:
            res |= self.get_closure(project)
        
        return res

    def get_group(self):
        # get the project group and the GO function to create the picture and the tables
        # C the group of the project
        helptable = {}
        C = [self.get_closure(self.BLRP)]

        # 0 - do not use, 1 - use already
        helptable[frozenset(C[0])] = 0
        GO = dict()
        while True:
            size = len(C)
            print("Project Group Size:", len(C), end = '\r')
            for index, group in enumerate(C.copy()):
                if helptable.get(frozenset(group)) == 1: continue
                for char in self.V_t | self.V_n:
                    res = self.goto(group, char)
                    if res:
                        if res not in C:
                            if not GO.get((index, char)):
                                GO[(index, char)] = len(C)
                                C.append(res)
                                helptable[frozenset(res)] = 0
                        else:
                            if res == group:
                                GO[(index, char)] = index
                            else:
                                if not GO.get((index, char)):
                                    GO[(index, char)] = C.index(res)
                helptable[frozenset(group)] = 1
            if len(C) == size: break
        return C, GO

    def init_table(self):
        # init the action and the goto table for the LR(1)
        # create action table
        action = {}
        goto   = {}
        for index, group in enumerate(self.group):
            for project in group:
                # for action
                left, right = project[0].split('->')
                creators = right.split()
                point_index = creators.index('·')
                if point_index + 1 < len(creators):
                    # shift
                    X = creators[point_index + 1]
                    if X in self.V_t:
                        if self.GO.get((index, X)):
                            action[(index, X)] = 'S' + str(self.GO.get((index, X)))
                    elif X in self.V_n:
                        # goto table
                        if self.GO.get((index, X)):
                            goto[(index, X)] = str(self.GO.get((index, X)))
                    else:
                        print('Meet the unexpected character!')
                        exit(0)
                else:
                    # reduce
                    # delete the ' ·'
                    string = project[0].strip()[:-2]
                    if len(string.split()) == 2:
                        string += ' @'
                    for jindex, rule in enumerate(self.rules):
                        if rule.strip() == string:
                            action[(index, project[1])] = 'r' + str(jindex)
        return action, goto

    def get_first(self, char):
        # get the first set of the special V_n
        if char in self.V_t or char == '@': 
            return set([char])
        elif char in self.V_n:
            # un terminal character, iter all the rules
            FIRST = set()
            for rule in self.rules:
                if rule.split('->')[0].strip() == char:
                    _, right = rule.split('->')
                    res = set(['@'])
                    index = 0
                    while '@' in res:
                        if index == len(right.split()): break
                        res = self.get_first(right.split()[index])
                        FIRST |= res
                        index += 1
            return FIRST
        else:
            print("Meet the character unexpected:", char)
            exit(1)

    def mainloop(self, infile, outfile):
        # the main control function for the LR analyse
        tree = ET.parse(infile)
        root = tree.getroot()
        # symbol is the list of the tuple (index, value, type, valid)
        symbols = [(token.find("number").text, token.find("value").text,\
                token.find("type").text, token.find("valid").text) \
                for token in root.iter("token")]
        symbols.append((-1, '#', -1, -1))

        state_stack  = [0]
        symbol_stack = ['#']

        # the index for the symbols to shift
        index = 0
        state = True
        while state:
            # error
            if symbols[index][3] == "False":
                print("Scaner find the error!")
                exit(1)

            # the main control using the table of the action or the goto table
            try:
                res = self.action[(state_stack[-1], self.transform(symbols[index]))]
                if res.startswith('S'):
                    # shift action
                    state_stack.append(int(res[1:]))
                    symbol_stack.append(self.transform(symbols[index]))
                    index += 1
                elif res.startswith('r'):
                    # redu# the index of the reduce action equalatioin
                    number = int(res[1:])
                    left, right = self.rules[number].split('->')
                    count = len(right.split())
                    # 0 case
                    if count == 1 and right.split()[0] == '@':
                        count = 0

                    # pop count times and push the reduce element
                    for i in range(count):
                        state_stack.pop()
                        symbol_stack.pop()
                    symbol_stack.append(left.strip())
                    state_stack.append(int(self.goto[(state_stack[-1], symbol_stack[-1])]))

                    # chaeck the acc
                    if number == 0: return True
                else:
                    print("Unexpected things happened:")
                    print(symbol_stack, symbols[index:])
                    return False
            except Exception as e:
                # check for end (acc)
                if symbol_stack[1] == self.begin_symbol: return True

                # the error
                print(e)
                print("parser find the error:")
                print('state stack:', state_stack)
                print('symbols stack:', symbol_stack)
                print('left symbols:', symbols[index:])
                return False

            # test print
            print(symbol_stack)

    def write_file(self):
        # write the analyse result into the XML file
        pass

    def write_table(self):
        # write the init file into the file
        # write the self.action, self, goto
        with open("table.pkl", 'wb') as f:
            pickle.dump([self.action, self.goto], f)

    def read_table(self):
        # read the data table from the file
        with open("table.pkl", 'rb') as f:
            self.action, self.goto = pickle.load(f)

    def transform(self, char):
        # transform table, char is the four-element tuple of fromthe token
        # (index, value, type, valid)
        if char[0] == -1 and char[1] == '#': return '#'
        elif char[2] == "identifier": return 'ID'
        elif char[2] == "constant": return 'CONST'
        elif char[2] == "operator": return char[1]
        elif char[2] == "separate": return char[1]
        elif char[2] == "keyword": return char[1]
        else:
            print("find the unexpected token:", char)
            exit(0)

if __name__ == "__main__":
    # change the depth of the recursive
    _, rule, infile, outfile = sys.argv
    app = LR(rule, "PROGRAM")
    # start the main control to run for the analysing
    if app.mainloop(infile, outfile):
        print("Parser the file successfully!")
