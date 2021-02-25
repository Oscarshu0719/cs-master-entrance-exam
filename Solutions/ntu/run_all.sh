#!/bin/bash

EXT=tex
for i in *.${EXT}; do
    xelatex "$i" -output-directory=doc
done
