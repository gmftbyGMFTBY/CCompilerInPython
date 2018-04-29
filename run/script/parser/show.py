#!/usr/bin/python3

'''
this python script try to create the png photo of the LR(1)
use the dot command in the system,  this is the only need to for running, just enjoying.
Thank you!

read the file to create the photo, the file format is:
       [node|Index]: [over|nornmal|acc|begin]
       project1
       project2
       project3
       ...

       [edge|Index]: c；
       index1 -> index2 : symbol1
       index2 -> index3 : symbol2
'''

import os

def draw(filename):
    fw = open(f"{filename}.gv", 'w')
    fw.write("digraph LR {\nrankdir=LR;\nsize=\"8.5\"\n\n")
    with open(filename, 'r') as f:
        buffer = []
        # state 0 - not the begining, state 1 - stop and wait for another
        state = 1
        nore  = 0   # this decide the node or the edge in the file, 0 - edge, > 0 node
                    # 1 begin , 2 over, 3 normal
        index = 0
        data = f.readlines()
        for line in data:
            if len(line.strip()) != 0:
                # this line is not empty
                buffer.append(line)
                state = 0
            else:
                # find the definantion of the node of the edge, try to write into the file
                state = 1
                decide = buffer[0].split(':')
                if len(decide) != 2:
                    print(decide)
                    print("Something wrong with the file:", filename)
                    exit(1)
                else:
                    _, index = decide[0][1:-1].split('|') 
                    if decide[1].strip():
                        if decide[1].strip() == '[begin]': nore = 1
                        elif decide[1].strip() == '[over]': nore = 2
                        elif decide[1].strip() == '[normal]': nore = 3
                        else:
                            print("Something wrong with the file:", filename)
                            exit(1)
                    else:
                        nore = 0

                    if nore > 0 :
                        label = ''.join(buffer[1:])
                        res = "node [shape = box, label=\"{l}\", fontsize = 10] {ind};\n".format(l=label, ind=index)
                        fw.write(res)
                    else:
                        string, symbol = buffer[1].split(':')
                        res = "{str} [label = \"{sym}\"];\n".format(str=string, sym=symbol)
                        fw.write(res)
                buffer = []
    fw.write('}\n')
    fw.close()

    # use dot in the system
    os.system(f"dot -Tpng {filename}.gv -o {filename}.png")


if __name__ == "__main__":
    draw("./test")
