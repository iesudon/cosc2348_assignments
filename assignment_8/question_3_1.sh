#!/bin/bash

goal=50
start=2
for i in $(seq $start $goal)
do
    count=0
    for j in $(seq 2 $(($i - 1)))
    do 
        if [ $(($i % $j)) -eq 0 ]
        then
            count=1
            break
        fi
    done
    if [ $count -eq 0 ]
    then
    echo $i
    fi
done
