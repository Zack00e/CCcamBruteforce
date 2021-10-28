#!/bin/bash
for num in {1..100}
do
    if ! python Generator.py ${num}; then      
        exit
    else
     python -m Checker
    fi
    exit
done

