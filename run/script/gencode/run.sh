#!/bin/bash

./scaner.py test.c test.token.xml

./parser.py ./rules test.token.xml test.parser.xml

python ./gencode.py > test.asm
