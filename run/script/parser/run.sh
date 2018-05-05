#!/bin/bash

./scaner.py test.c test.token.xml

./parser.py ./rule/rules test.token.xml test.parser.xml
