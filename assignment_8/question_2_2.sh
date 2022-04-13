#!/bin/bash
sum=20
while [[ ! $sum -ge 40 ]]
do
    echo $sum
    let sum++
done
echo $sum