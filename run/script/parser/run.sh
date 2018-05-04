#!/bin/bash

./scaner.py test.c test.token.xml

./parser.py ./rule/test test.token.xml test.parser.xml
