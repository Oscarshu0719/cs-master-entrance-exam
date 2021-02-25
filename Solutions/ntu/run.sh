#!/bin/bash

for i in $*; do 
    xelatex "$i" -output-directory=doc
done
