#!/bin/bash
sum=20
for i in $(seq 20 39)
do
    echo $sum
    let sum++
done
echo $sum