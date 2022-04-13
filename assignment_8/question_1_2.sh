#!/bin/bash
i=1
until [ ! $i -le 15 ]
do 
    echo $i
    let i++
done
