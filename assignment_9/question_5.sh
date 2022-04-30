#!/bin/bash
for i in $(seq 1 2 50)
do
    arrodd[i]=$(($arrodd+$i))
done
echo ${arrodd[@]}
echo "-------"
for j in $(seq 2 2 50)
do
    arreven[j]=$(($arreven+$j))

done
echo ${arreven[@]}
