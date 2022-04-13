#!/bin/bash
sum=20
while [[ $sum -le 39 ]]
do
    echo $sum
    let sum++
done
echo $sum
