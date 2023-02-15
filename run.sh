#!/bin/bash

cp ./text.txt text-holder/text.txt

rm *.txt

cp text-holder/text.txt ./text.txt

python3 main.py