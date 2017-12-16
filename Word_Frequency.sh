#!bin/bash

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r
