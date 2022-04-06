#!/bin/bash

randint=$$ # create random number

if [[ $((randint%100)) -gt 100 || $((randint%100)) -lt 0 ]] #if less than 0 and greater than 100
then
    echo -e "Invalid value"
elif [[ $((randint%100)) -le 100 && $((randint%100)) -ge 90 ]] #if less than or equal 100 and greater than or equal to 90
then
    echo -e "A"
elif [[ $((randint%100)) -ge 80 && $((randint%100)) -le 89 ]] #if less than or equal 80 and greater than or equal to 89
then
    echo -e "B"
elif [[ $((randint%100)) -ge 70 &&  $((randint%100)) -le 79 ]] #if less than or equal 79 and greater than or equal to 70
then
    echo -e "C"
elif [[ $((randint%100)) -ge 60 && $((randint%100)) -le 69 ]] #if less than or equal 69 and greater than or equal to 60
then
    echo -e "D"
elif [[ $((randint%100)) -lt 60 ]]
then
    echo -e "Fail"
else
    echo -e "Something went wrong" #something went wrong
fi #end if
