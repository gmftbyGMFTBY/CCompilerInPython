#!/home/lantian/anaconda3/bin/python
# Author: GMFTBY
# Time  : 2018.4.29

'''
Use LR(1) Algorithm to create the parser of the C language.
As we know, the standard C language is the LR(1) language.

The only constrant of the rule is that the first rule must be the last element
of the whole rules.
'''

import pydot, pprint, sys, pickle
import xml.etree.ElementTree as ET
from lxml import etree

class LR:
    def __init__(self, filename):
        # read the file of the rules
        with open(filename, 'r') as f:
            # filte the comment of the file `rules`
            self.rules = list(map(lambda line: line[:-1], \
                    filter(lambda line: False if line[:2] == "//" \
                    or not line.strip() else True, f.readlines())))

            # begin_symbol, must be the left of the first rule
            left, _ = self.rules[0].split('->')
            self.begin_symbol = left.strip()
            
            # self.rules_bag = self.get_rules_bag()
            for rule in self.rules:
                if rule.split('->')[0].strip() == self.begin_symbol:
                    _, right = rule.split('->')
                    right = '·' + right
                    self.BLRP = (self.begin_symbol + ' -> ' + right, '#')
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
        self.draw()
        # self.read_table()
        print("Init the LR(1) analyser table successfully!")

    def draw(self):
        g = pydot.Dot(graph_type="digraph", rankdir="LR")
        nodes = []    # save the nodes

        for index, group in enumerate(self.group):
            string = r'\n'.join([f'{project[0]}, {project[1]}' for project in group])
            node = pydot.Node(str(index), shape="box", label=string)
            g.add_node(node)
            nodes.append(node)

        for index, item in enumerate(self.GO.items()):
            key, value = item
            g.add_edge( pydot.Edge(nodes[key[0]], nodes[value], label=key[1]) )

        g.write_png('./res.png')

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

if __name__ == "__main__":
    # change the depth of the recursive
    if len(sys.argv) > 2: 
        print('Too much parameters!')
        exit(1)
    rule = sys.argv[1]
    app = LR(rule)
