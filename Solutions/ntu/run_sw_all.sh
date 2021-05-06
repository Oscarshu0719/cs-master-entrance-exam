#!/bin/bash

for i in $(ls | egrep -i 'ntu_[\d\d\d]_sw_sol.tex'); do
    xelatex "$i" -output-directory=doc
done
