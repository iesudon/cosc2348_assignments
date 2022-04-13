#!/bin/bash

var_test=21
#ranges 1 to 10, 11 to 20, more

if [[ $var_test -ge 1 && $var_test -le 10 ]]
then
echo "Between 1 to 10"
elif [[ $var_test -ge 11 && $var_test -le 20 ]]
then
echo "Between 11 to 20"
elif [[ $var_test -gt 20 ]]
then
echo "greater than 20"
else
echo "less than 1"
fi


