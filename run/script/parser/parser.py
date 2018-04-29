#!/usr/bin/python3
# Author: GMFTBY
# Time  : 2018.4.29

'''
Use LR(1) Algorithm to create the parser of the C language.
'''

import sys
import pprint

class LR:
    def __init__(self, filename, Begin_symbol):
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
        print('-' * 50)
        pprint.pprint(self.goto(self.get_closure(self.BLRP), '='))
        # init the action and the goto table
        self.init_table()
        # print("Init the LR(1) analyser table successfully!")

    def get_character(self):
        V_t = set(['*', '=', 'i'])
        V_n = set(['S', "S'", 'L', 'R'])
        # ...
        return V_t, V_n
    
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
                if index + 2 < length: beta = creators[index + 2]
                else: beta = None

                if not B:
                    # do not have the B, end get closure
                    continue
                else:
                    if beta: 
                        res = self.get_first(beta)
                        if 'e' in res:
                            searcher = set(res) | set([project[1]])
                        else:
                            searcher = set(res)
                    else:
                        searcher = set([project[1]])
                        
                    for rule in self.rules:
                        if rule.split('->')[0].strip() == B:
                            _, right = rule.split('->')
                            if len(right.split()) == 1 and right.split()[0] == 'e': right = '·'
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
        C = [self.get_closure(self.BLRP)]
        GO = dict()
        while True:
            size = len(C)
            for index, group in enumerate(C.copy()):
                for char in self.V_t | self.V_n:
                    res = self.goto(group, char)
                    if res:
                        if res not in C:
                            C.append(res)
                            GO[index] = (len(C) - 1, char)
                        else:
                            GO[index] = (index, char)
            if len(C) == size: break
        return C, GO

    def init_table(self):
        # init the action and the goto table for the LR(1)
        pass

    def get_first(self, char):
        # get the first set of the special V_n
        if self.IsV_t(char) or char == 'e': return set(char)
        elif self.IsV_n(char):
            # un terminal character, iter all the rules
            FIRST = set()
            for rule in self.rules:
                if rule.split()[0].strip() == char:
                    _, right = rule.split('->')
                    res = {'e'}
                    index = 0
                    while 'e' in res:
                        if index == len(right.split()): break
                        FIRST |= res
                        res = self.get_first(right.split()[index])
                        index += 1
                    FIRST |= res
            return FIRST
        else:
            print("Meet the character unexpected:", char)
            exit(1)

    def mainloop(self):
        # the main control function for the LR analyse
        pass

    def write_file(self):
        # write the analyse result into the XML file
        pass

    def IsV_t(self, char):
        # check the terminal character
        if char in self.V_t: return True
        else: return False

    def IsV_n(self, char):
        # check the un terminal character
        if char in self.V_n: return True
        else: return False

if __name__ == "__main__":
    app = LR('./rules', "S'")
    # start the main control to run for the analysing
    app.mainloop()
    app.write_file()
